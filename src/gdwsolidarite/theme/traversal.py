# -*- coding: utf-8 -*-

from plone import api
from zope.interface import Interface
from zope.publisher.interfaces.http import IHTTPRequest
from zope.component import adapts
from ZPublisher.BaseRequest import DefaultPublishTraverse

RESTRICTED_PAGES = ['sitemap', 'accessibility-info']


class RestrictTraversable(DefaultPublishTraverse):
    """
    """
    adapts(Interface, IHTTPRequest)

    def publishTraverse(self, request, name):
        """
        Avoid traversing to other pages / views in the Plone site
        """
        if name in RESTRICTED_PAGES:
            url = api.portal.get().absolute_url()
            request.response.redirect(url)
            return ''
        return super(RestrictTraversable, self).publishTraverse(request, name)
