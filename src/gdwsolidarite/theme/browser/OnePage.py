# -*- coding: UTF-8 -*-

from Products.Five import BrowserView


class OnePageView(BrowserView):

    def getPageText(self, pageId):
        page = getattr(self.context, pageId, None)
        if page is None:
            return
        return page.getText()
