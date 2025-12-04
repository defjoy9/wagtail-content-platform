from django import template

register = template.Library()


@register.filter(name='reading_time')
def reading_time(word_count):
    """
    Calculate reading time in minutes based on word count.
    Assumes average reading speed of 200 words per minute.
    """
    try:
        words = int(word_count)
        minutes = max(1, round(words / 200))
        return minutes
    except (ValueError, TypeError):
        return 1
