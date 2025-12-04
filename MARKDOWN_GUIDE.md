# Markdown Blog Guide

Your blog now supports full Markdown syntax! Here's what you can do:

## Basic Formatting

```markdown
**bold text**
*italic text*
~~strikethrough~~
`inline code`
```

## Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
```

## Lists

```markdown
- Bullet point 1
- Bullet point 2
  - Nested item

1. Numbered item 1
2. Numbered item 2
```

## Links and Images

```markdown
[Link text](https://example.com)
![Image alt text](image-url.jpg)
```

## Code Blocks with Syntax Highlighting

The most important feature - code blocks with the macOS terminal look!

### Python Example
\`\`\`python
def hello_world():
    print("Hello, World!")
    return True
\`\`\`

### JavaScript Example
\`\`\`javascript
function greet(name) {
    console.log(`Hello, ${name}!`);
    return true;
}
\`\`\`

### Bash/Shell Example
\`\`\`bash
#!/bin/bash
echo "Hello World"
npm install
python manage.py runserver
\`\`\`

### Other Languages
Supported languages include:
- `python`, `javascript`, `typescript`, `jsx`, `tsx`
- `bash`, `sh`, `zsh`, `shell`
- `html`, `css`, `scss`, `sass`
- `json`, `yaml`, `toml`
- `sql`, `graphql`
- `java`, `c`, `cpp`, `csharp`, `go`, `rust`
- `php`, `ruby`, `swift`, `kotlin`
- And many more!

## Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

## Blockquotes

```markdown
> This is a blockquote
> It can span multiple lines
```

## Horizontal Rules

```markdown
---
```

## Notion Code Block Compatibility

When you copy code from Notion:
1. Paste it directly into your markdown editor
2. Make sure it's wrapped in triple backticks with the language
3. The macOS-style code blocks will automatically:
   - Show red, yellow, green circles (like macOS Terminal)
   - Include a "Copy" button
   - Apply syntax highlighting
   - Be easy to copy/paste

Example of what to paste from Notion:
\`\`\`python
# Your Notion code here
def example():
    pass
\`\`\`

The code will render with:
- ✅ macOS terminal-style header
- ✅ Traffic light buttons (red, yellow, green)
- ✅ Copy button with icon
- ✅ Syntax highlighting (VS Code Dark+ theme)
- ✅ Easy one-click copy functionality

## Tips

1. **Line breaks**: Use two spaces at the end of a line or press Enter twice for a new paragraph
2. **Escape characters**: Use backslash `\` to escape special markdown characters
3. **Preview**: The Wagtail admin editor shows live preview as you type
4. **Code languages**: Always specify the language after triple backticks for proper syntax highlighting

## Example Blog Post

```markdown
# My Amazing Tutorial

Welcome to this tutorial! Here's what we'll cover:

1. Setup
2. Implementation
3. Testing

## Installation

First, install the required packages:

\`\`\`bash
pip install django wagtail
python manage.py migrate
\`\`\`

## Python Implementation

Here's the main code:

\`\`\`python
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title
\`\`\`

> **Note**: Remember to run migrations after creating models!

## Conclusion

That's it! You now have a working blog. Check out [the docs](https://docs.djangoproject.com) for more info.
```
