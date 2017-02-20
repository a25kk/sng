# -*- coding: utf-8 -*-
"""Module providing views for the site navigation root"""
from Products.Five.browser import BrowserView
from Products.ZCatalog.interfaces import ICatalogBrain
from plone import api
from plone.app.contentlisting.interfaces import IContentListing
from plone.app.contentlisting.interfaces import IContentListingObject
from plone.app.contenttypes.interfaces import INewsItem
from zope.component import getMultiAdapter
from zope.component import getUtility

from sng.sitecontent.contentpage import IContentPage
from sng.sitecontent.interfaces import IResponsiveImagesTool

IMG = 'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs='


class LandingPageView(BrowserView):
    """ Landing page

    Dedicated view to hold a live search and potential introduction
    """


class FrontPageView(BrowserView):
    """ General purpose frontpage view """

    def __call__(self):
        self.has_newsitems = len(self.recent_news()) > 0
        self.has_preview_cards = len(self.preview_cards()) > 0
        return self.render()

    def render(self):
        return self.index()

    def preview_cards(self):
        portal = api.portal.get()
        news_folder = portal['news']
        items = api.content.find(
            context=news_folder,
            depth=2,
            object_provides=IContentPage.__identifier__,
            review_state='published',
            sort_on='Date',
            sort_order='reverse',
            sort_limit=10)
        return items

    def can_edit(self):
        show = False
        if not api.user.is_anonymous():
            show = True
        return show

    def portal_id(self):
        portal = api.portal.get()
        return portal.id

    def recent_news(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        items = catalog(object_provides=INewsItem.__identifier__,
                        review_state='published',
                        sort_on='Date',
                        sort_order='reverse',
                        sort_limit=10)[:10]
        return IContentListing(items)

    def section_preview(self, section):
        info = {}
        if section.startswith('/'):
            target = section
        else:
            target = '/{0}'.format(section)
        item = api.content.get(path=target)
        if item:
            info['title'] = item.Title()
            info['teaser'] = item.Description()
            info['url'] = item.absolute_url()
            info['image'] = self.image_tag(item)
            info['subitems'] = None
            if target in ('/news'):
                info['subitems'] = self.recent_news()
        return info

    def get_image_data(self, uuid):
        tool = getUtility(IResponsiveImagesTool)
        return tool.create(uuid)

    def image_tag(self, item):
        data = {}
        sizes = ['small', 'medium', 'large']
        idx = 0
        for size in sizes:
            idx += 0
            img = self._get_scaled_img(item, size)
            data[size] = '{0} {1}w'.format(img['url'], img['width'])
        return data

    def _get_scaled_img(self, item, size):
        if (
            ICatalogBrain.providedBy(item) or
            IContentListingObject.providedBy(item)
        ):
            obj = item.getObject()
        else:
            obj = item
        info = {}
        if hasattr(obj, 'image'):
            scales = getMultiAdapter((obj, self.request), name='images')
            if size == 'small':
                scale = scales.scale('image', width=300, height=300)
            if size == 'medium':
                scale = scales.scale('image', width=600, height=600)
            else:
                scale = scales.scale('image', width=900, height=900)
            if scale is not None:
                info['url'] = scale.url
                info['width'] = scale.width
                info['height'] = scale.height
        else:
            info['url'] = IMG
            info['width'] = '1px'
            info['height'] = '1px'
        return info