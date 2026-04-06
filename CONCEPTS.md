# Notes of Md files syntaxes
Ah, you want the actual Markdown syntax cheat sheet—how to format the text itself. Here are the core commands you need to build `.md` files.

### 1. Headings
Use `#` to create headings. More hashes equal a smaller heading.
```markdown
# H1 (Main Title)
## H2 (Section)
### H3 (Sub-section)
```

### 2. Text Formatting
Use asterisks or tildes to emphasize text.
```markdown
**Bold text**
*Italic text*
~~Strikethrough~~
```

### 3. Lists
Use hyphens for bullets and numbers for ordered lists. Indent to nest them.
```markdown
- Bullet point
- Another point
  - Nested point (indent with 2 spaces)

1. First step
2. Second step
```

### 4. Code
Use backticks for technical notes or scripts.
```markdown
This is `inline code` for small variables.

```python
# This is a multi-line code block. 
# Adding 'python' adds syntax highlighting.
x = 10
```
*(Note: Close the block with three backticks)*

### 5. Links and Checkboxes
Highly useful for your progress trackers.
```markdown
[Clickable Link Text](https://google.com)

- [x] Completed task
- [ ] Pending task
```

### 6. Blockquotes & Dividers
Use `>` for callouts and `---` to separate sections.
```markdown
> Use this to highlight a critical insight or pattern.

---
```


# Notes and keypoints

- bool of anything is 1 but 0.
- taking multiple inputs in a single line = x,y,z = (input("Enter the 3 numbers separated via space: ").split()
)
  - this takes str as input 
- isinstance(object, classinfo) returns True if the object is an instance of the specified class.
- In Python, constants are written in ALL_CAPS by convention.
