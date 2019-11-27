# -*- coding: utf-8 -*-
"""Module providing configuration for element display"""
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from sng.sitecontent import MessageFactory as _


available_card_sizes = SimpleVocabulary(
    [SimpleTerm(value=u'100', title=_(u'100')),
     SimpleTerm(value=u'75', title=_(u'3/4')),
     SimpleTerm(value=u'66', title=_(u'2/3')),
     SimpleTerm(value=u'50', title=_(u'1/2')),
     SimpleTerm(value=u'33', title=_(u'1/3')),
     SimpleTerm(value=u'25', title=_(u'1/4'))
     ]
)


@provider(IFormFieldProvider)
class IDisplayOptions(model.Schema):
    """Behavior providing selectable grid sizes"""

    model.fieldset(
        'display',
        label=u"Display",
        fields=['elementSize']
    )

    elementSize = schema.Choice(
        title=_(u"Select Display Size"),
        description=_(u"When displaying the content page inside a grid or "
                      u"card preview layout on a landing page the selected "
                      u"sizes will be used for alignment"),
        vocabulary=available_card_sizes,
        required=False,
    )


@implementer(IDisplayOptions)
@adapter(IDexterityContent)
class DisplayOptions(object):

    def __init__(self, context):
        self.context = context
