# -*- coding: utf-8 -*-

from zope.component import getUtility
from zope.component import getMultiAdapter
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.portlets.interfaces import IPortletManager, \
                                      IPortletAssignmentMapping, \
                                      ILocalPortletAssignmentManager
from Products.CMFCore.utils import getToolByName


def setupSite(context):
    if context.readDataFile('gdwsolidarite.theme_various.txt') is None:
        return
    portal = context.getSite()

    clearPortlets(portal)
    deleteContent(portal, 'Members')
    deleteContent(portal, 'news')
    deleteContent(portal, 'events')
    deleteContent(portal, 'front-page')
    createDocument(portal, 'action', 'Action')
    createDocument(portal, 'partenaires', 'Partenaires')
    createDocument(portal, 'hebergements', 'Hébergements')
    createDocument(portal, 'a-propos', 'A propos')
    createDocument(portal, 'nous-suivre', 'Nous suivre')
    changeFolderView(portal, portal, 'one_page_view')


def createDocument(parentFolder, documentId, documentTitle, description=''):
    if documentId not in parentFolder.objectIds():
        parentFolder.invokeFactory('Document', documentId, title=documentTitle,
                                   description=description)
    createdDoc = getattr(parentFolder, documentId)
    publishObject(createdDoc)
    createdDoc.reindexObject()
    return createdDoc


def deleteContent(portal, objIf):
    content = getattr(portal, objIf, None)
    if content is not None:
        portal.manage_delObjects(objIf)


def changeFolderView(portal, folder, viewname):
    addViewToType(portal, 'Folder', viewname)
    if folder.getLayout() != viewname:
        folder.setLayout(viewname)


def addViewToType(portal, typename, templatename):
    pt = getToolByName(portal, 'portal_types')
    foldertype = getattr(pt, typename)
    available_views = list(foldertype.getAvailableViewMethods(portal))
    if not templatename in available_views:
        available_views.append(templatename)
        foldertype.manage_changeProperties(view_methods=available_views)


def publishObject(obj):
    portal_workflow = getToolByName(obj, 'portal_workflow')
    if portal_workflow.getInfoFor(obj, 'review_state') in ['visible', 'private']:
        portal_workflow.doActionFor(obj, 'publish')
    return


def clearPortlets(folder):
    clearColumnPortlets(folder, 'left')
    clearColumnPortlets(folder, 'right')


def clearColumnPortlets(folder, column):
    manager = getManager(folder, column)
    assignments = getMultiAdapter((folder, manager), IPortletAssignmentMapping)
    for portlet in assignments:
        del assignments[portlet]
    assignable = getMultiAdapter((folder, manager), ILocalPortletAssignmentManager)
    assignable.setBlacklistStatus(CONTEXT_CATEGORY, True)


def getManager(folder, column):
    if column == 'left':
        manager = getUtility(IPortletManager, name=u'plone.leftcolumn', context=folder)
    else:
        manager = getUtility(IPortletManager, name=u'plone.rightcolumn', context=folder)
    return manager
