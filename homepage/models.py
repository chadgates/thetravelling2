from django.db import models

# Create your models here.
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel, FieldRowPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel

# Contact Form
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.wagtailforms.models import AbstractFormField
from modelcluster.fields import ParentalKey

# Blocks
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock



class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(WagtailCaptchaEmailForm):
    intro = RichTextField(blank=True, help_text='Edit the content you want to see before the form.')
    thank_you_text = RichTextField(blank=True, help_text='Set the message users will see after submitting the form.')

    class Meta:
        verbose_name = "Form submission page"

    content_panels = WagtailCaptchaEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        MultiFieldPanel([
            FieldPanel('to_address', classname="full"),
            FieldPanel('from_address', classname="full"),
            FieldPanel('subject', classname="full"),
        ], "Email")
    ]


class CoupleBlock(blocks.StructBlock):
    maintitle = blocks.CharBlock()
    subtitle = blocks.CharBlock()
    headline = blocks.CharBlock()

    bridename = blocks.CharBlock()
    bridetext = blocks.TextBlock()
    bridephoto = ImageChooserBlock()

    groomame = blocks.CharBlock()
    groomtext = blocks.TextBlock()
    groomphoto = ImageChooserBlock()

    class Meta:
        template = 'homepage/couple_block.html'
        icon = 'placeholder'
        label = 'Couple Block'


class ImpressumPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]


class BlockPage(Page):
    body = StreamField(
        [('CoupleBlock', CoupleBlock()),
         ], default="")

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

class HomePage(Page):

    YEAR_CHOICES = (
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
    )

    MONTH_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    DAY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    )
    HOUR_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
    )
    MINSEC_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48'),
        ('49', '49'),
        ('50', '50'),
        ('51', '51'),
        ('52', '52'),
        ('53', '53'),
        ('54', '54'),
        ('55', '55'),
        ('56', '56'),
        ('57', '57'),
        ('58', '58'),
        ('59', '59'),
    )


    background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    couplename = models.CharField(max_length=255, default="Someone & Someone")
    subtitle = models.CharField(max_length=255, blank=True, default="We are getting married")
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default="2017")
    month = models.CharField(max_length=2, choices=MONTH_CHOICES, default="7")
    day = models.CharField(max_length=2, choices=DAY_CHOICES, default="1")
    hour = models.CharField(max_length=2, choices=HOUR_CHOICES, default="12")
    minute = models.CharField(max_length=2, choices=MINSEC_CHOICES, default="0")
    seconds = models.CharField(max_length=2, choices=MINSEC_CHOICES, default="0")
    icsfile = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = StreamField(
        [('CoupleBlock', CoupleBlock()),
         ], default="")

    content_panels = Page.content_panels + [
        FieldPanel('couplename', classname="full"),
        FieldPanel('subtitle', classname="full"),
        FieldRowPanel([
                    FieldPanel('year'),
                    FieldPanel('month'),
                    FieldPanel('day'),
                    FieldPanel('hour'),
                    FieldPanel('minute'),
                    FieldPanel('seconds')
        ]),
        ImageChooserPanel('background'),
        DocumentChooserPanel('icsfile'),
        StreamFieldPanel('body'),
    ]
