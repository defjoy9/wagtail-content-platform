from django import template

register = template.Library()


@register.filter(name='reading_time')
def reading_time(word_count):
    """
    Calculate estimated reading time in minutes.
    
    Assumes average reading speed of 200 words per minute for technical content.
    Returns minimum of 1 minute for short posts.
    
    Args:
        word_count: Integer or string representation of word count
        
    Returns:
        Integer representing estimated reading time in minutes
        
    Example:
        {{ post.body|wordcount|reading_time }} outputs "5 min read" for ~1000 words
    """
    try:
        words = int(word_count)
        minutes = max(1, round(words / 200))
        return minutes
    except (ValueError, TypeError):
        return 1
