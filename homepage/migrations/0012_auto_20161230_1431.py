# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 14:31
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20161230_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('CoupleBlock', wagtail.wagtailcore.blocks.StructBlock((('bg_gray', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Select if background should by gray', required=False)), ('maintitle', wagtail.wagtailcore.blocks.CharBlock()), ('subtitle', wagtail.wagtailcore.blocks.CharBlock()), ('headline', wagtail.wagtailcore.blocks.CharBlock()), ('bridename', wagtail.wagtailcore.blocks.CharBlock()), ('bridetext', wagtail.wagtailcore.blocks.TextBlock()), ('bridephoto', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('groomame', wagtail.wagtailcore.blocks.CharBlock()), ('groomtext', wagtail.wagtailcore.blocks.TextBlock()), ('groomphoto', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('TwoColumnBlock', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('theme-white', 'White'), ('theme-black', 'Black'), ('theme-darker', 'Dark Gray'), ('theme-body-color', 'Body Color'), ('theme-primary', 'Primary Color'), ('theme-secondary', 'Secondary Color')], default='white')), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_width', wagtail.wagtailcore.blocks.CharBlock(default='600', max_length=4, required=True)), ('map_height', wagtail.wagtailcore.blocks.CharBlock(default='450', max_length=4, required=True)), ('map_params', wagtail.wagtailcore.blocks.CharBlock(help_text='No spaces, add + instead', max_length=300, required=True)))))), icon='arrow-left', label='Left column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_width', wagtail.wagtailcore.blocks.CharBlock(default='600', max_length=4, required=True)), ('map_height', wagtail.wagtailcore.blocks.CharBlock(default='450', max_length=4, required=True)), ('map_params', wagtail.wagtailcore.blocks.CharBlock(help_text='No spaces, add + instead', max_length=300, required=True)))))), icon='arrow-right', label='Right column content'))))), ('GoogleMapBlock', wagtail.wagtailcore.blocks.StructBlock((('map_width', wagtail.wagtailcore.blocks.CharBlock(default='600', max_length=4, required=True)), ('map_height', wagtail.wagtailcore.blocks.CharBlock(default='450', max_length=4, required=True)), ('map_params', wagtail.wagtailcore.blocks.CharBlock(help_text='No spaces, add + instead', max_length=300, required=True))))), ('RichTextBlock', wagtail.wagtailcore.blocks.RichTextBlock()), ('TimeLineBlock', wagtail.wagtailcore.blocks.StructBlock((('bg_gray', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Select if background should by gray', required=False)), ('headline', wagtail.wagtailcore.blocks.CharBlock()), ('maintitle', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('timelineentry', wagtail.wagtailcore.blocks.StreamBlock((('TimelineEntry', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock()), ('date', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock())))),), default='')))))), default=''),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('CoupleBlock', wagtail.wagtailcore.blocks.StructBlock((('bg_gray', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Select if background should by gray', required=False)), ('maintitle', wagtail.wagtailcore.blocks.CharBlock()), ('subtitle', wagtail.wagtailcore.blocks.CharBlock()), ('headline', wagtail.wagtailcore.blocks.CharBlock()), ('bridename', wagtail.wagtailcore.blocks.CharBlock()), ('bridetext', wagtail.wagtailcore.blocks.TextBlock()), ('bridephoto', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('groomame', wagtail.wagtailcore.blocks.CharBlock()), ('groomtext', wagtail.wagtailcore.blocks.TextBlock()), ('groomphoto', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('TimeLineBlock', wagtail.wagtailcore.blocks.StructBlock((('bg_gray', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Select if background should by gray', required=False)), ('headline', wagtail.wagtailcore.blocks.CharBlock()), ('maintitle', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('timelineentry', wagtail.wagtailcore.blocks.StreamBlock((('TimelineEntry', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock()), ('date', wagtail.wagtailcore.blocks.CharBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock())))),), default='')))))), default=''),
        ),
        migrations.AlterField(
            model_name='ourdaypage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('TwoColumnBlock', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('theme-white', 'White'), ('theme-black', 'Black'), ('theme-darker', 'Dark Gray'), ('theme-body-color', 'Body Color'), ('theme-primary', 'Primary Color'), ('theme-secondary', 'Secondary Color')], default='white')), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_width', wagtail.wagtailcore.blocks.CharBlock(default='600', max_length=4, required=True)), ('map_height', wagtail.wagtailcore.blocks.CharBlock(default='450', max_length=4, required=True)), ('map_params', wagtail.wagtailcore.blocks.CharBlock(help_text='No spaces, add + instead', max_length=300, required=True)))))), icon='arrow-left', label='Left column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('map_width', wagtail.wagtailcore.blocks.CharBlock(default='600', max_length=4, required=True)), ('map_height', wagtail.wagtailcore.blocks.CharBlock(default='450', max_length=4, required=True)), ('map_params', wagtail.wagtailcore.blocks.CharBlock(help_text='No spaces, add + instead', max_length=300, required=True)))))), icon='arrow-right', label='Right column content'))))), ('EventBlock', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock()), ('maintitle', wagtail.wagtailcore.blocks.CharBlock()), ('lefttitle', wagtail.wagtailcore.blocks.CharBlock()), ('lefttime', wagtail.wagtailcore.blocks.CharBlock()), ('leftdate', wagtail.wagtailcore.blocks.CharBlock()), ('leftext', wagtail.wagtailcore.blocks.TextBlock()), ('righttitle', wagtail.wagtailcore.blocks.CharBlock()), ('righttime', wagtail.wagtailcore.blocks.CharBlock()), ('rightdate', wagtail.wagtailcore.blocks.CharBlock()), ('righttext', wagtail.wagtailcore.blocks.TextBlock()))))), default=''),
        ),
    ]