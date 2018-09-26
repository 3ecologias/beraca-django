from modeltranslation.translator import register, TranslationOptions
from core.models import BlogPost, ServiceItem, ServiceMethod, ServiceIcons, PortfolioItem, Fullwidth_slider_item, AboutSection, AboutInternal

@register(BlogPost)
class BlogPostTranslation(TranslationOptions):
    fields = ('title', 'sub_title', 'intro', 'content', 'tag')

@register(ServiceItem)
class ServiceItemTranslation(TranslationOptions):
    fields = ('title', 'mention', 'abstract', 'conclusion', 'description')

@register(ServiceMethod)
class ServiceMethodTranslation(TranslationOptions):
    fields = ('title', 'desc')

@register(PortfolioItem)
class PortfolioItemTranslation(TranslationOptions):
    fields = ('title', 'sub_title', 'study', 'results', 'experience', 'tag')

@register(Fullwidth_slider_item)
class Fullwidth_slider_itemTranslation(TranslationOptions):
    fields = ('first_phrase', 'second_phrase')

@register(AboutSection)
class AboutSectionTranslation(TranslationOptions):
    fields = ('title', 'mention', 'first_content', 'second_content')

@register(AboutInternal)
class AboutInternalTranslation(TranslationOptions):
    fields = ('title', 'subtitle', 'title_paragraph', 'content', 'director', 'council', 'mission', 'vision', 'values')
