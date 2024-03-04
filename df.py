import pandas as pd

# Create the data dictionary
data = {
    'HTML Tag': [
        '<div>', '<a>', '<p>', '<span>', '<img>', '<ul>', '<li>', '<h1>, <h2>, ..., <h6>', '<input>', '<table>',
        '<tr>', '<td>', '<form>', '<button>', '<iframe>', '<script>', '<label>', '<select>', '<option>',
        '<strong>', '<em>', '<blockquote>', '<cite>', '<iframe>', '<code>', '<pre>', '<meta>', '<style>',
        '<textarea>', '<abbr>', '<footer>', '<header>', '<nav>', '<section>', '<aside>', '<article>',
        '<main>', '<time>', '<address>', '<hr>', '<br>', '<del>', '<ins>', '<sup>', '<sub>', '<svg>', '<canvas>'
    ],
    'Usage': [
        'Container', 'Anchor', 'Paragraph', 'Inline container', 'Image', 'Unordered list', 'List item', 'Headings',
        'Input field', 'Table', 'Table row', 'Table data/cell', 'Form', 'Button', 'Inline frame', 'Script',
        'Form label', 'Dropdown select', 'Option in select', 'Strong/bold text', 'Emphasized text', 'Blockquote',
        'Citation', 'Inline frame', 'Code', 'Preformatted text', 'Metadata', 'CSS style', 'Text area', 'Abbreviation',
        'Footer', 'Header', 'Navigation', 'Section', 'Aside content', 'Article', 'Main content', 'Time element',
        'Address', 'Horizontal rule', 'Line break', 'Deleted text', 'Inserted text', 'Superscript', 'Subscript',
        'SVG', 'Canvas'
    ],
    'Description': [
        'Defines a division or section in an HTML document.', 'Creates a hyperlink to another webpage or resource.',
        'Defines a paragraph of text.', 'Defines a section of inline content.', 'Embeds an image in an HTML document.',
        'Defines an unordered (bulleted) list.', 'Defines a single item in a list.',
        'Defines headings of varying sizes and importance.', 'Creates an input control, such as a text field or button.',
        'Defines a table in an HTML document.', 'Defines a row in an HTML table.', 'Defines a cell in an HTML table.',
        'Creates a form for user input.', 'Defines a clickable button.', 'Embeds another HTML document within the current one.',
        'Embeds or references a JavaScript code.', 'Defines a label for an input element.', 'Creates a dropdown selection list.',
        'Defines an option in a select dropdown list.', 'Emphasizes text strongly, typically displayed in bold.',
        'Emphasizes text, typically displayed in italics.', 'Defines a block quotation.', 'Defines the title of a work (e.g., book, movie)',
        'Embeds another HTML document within the current one.', 'Defines a piece of computer code.', 'Defines preformatted text, preserving whitespace.',
        'Provides metadata about the HTML document.', 'Defines CSS styles for an HTML document.', 'Creates a multiline text input control.',
        'Defines an abbreviation or acronym.', 'Defines a footer for a document or section.', 'Defines a header for a document or section.',
        'Defines navigation links in a document.', 'Defines a section in a document.', 'Defines content aside from the main content.',
        'Defines an independent, self-contained piece of content.', 'Defines the main content of a document.', 'Represents a specific time or date.',
        'Defines contact information for the author/owner of a document.', 'Represents a thematic break between paragraphs.',
        'Inserts a single line break.', 'Indicates deleted text in a document.', 'Indicates inserted text in a document.',
        'Renders text in superscript.', 'Renders text in subscript.', 'Embeds scalable vector graphics in an HTML document.',
        'Creates an area for drawing graphics with JavaScript.'
    ],
    'Example': [
        '<div>This is a div element</div>', '<a href="https://example.com">Example Link</a>',
        '<p>This is a paragraph.</p>', '<span>This is inline content.</span>',
        '<img src="image.jpg" alt="Image Description">', '<ul><li>Item 1</li><li>Item 2</li></ul>',
        '<ul><li>Item 1</li><li>Item 2</li></ul>', '<h1>This is a Heading</h1>',
        '<input type="text" placeholder="Enter text">', '<table><tr><td>Cell 1</td><td>Cell 2</td></tr></table>',
        '<table><tr><td>Cell 1</td><td>Cell 2</td></tr></table>', '<table><tr><td>Cell 1</td><td>Cell 2</td></tr></table>',
        '<form action="/submit" method="post">Form Content</form>', '<button>Click Me</button>',
        '<iframe src="https://example.com"></iframe>', '<script>alert("Hello, world!");</script>',
        '<label for="inputField">Input Label</label>',
        '<select><option value="1">Option 1</option><option value="2">Option 2</option></select>',
        '<select><option value="1">Option 1</option><option value="2">Option 2</option></select>',
        '<strong>This text is bold</strong>', '<em>This text is italicized</em>',
        '<blockquote>This is a quotation.</blockquote>', '<cite>The Great Gatsby</cite>',
        '<iframe src="https://example.com"></iframe>', '<code>print("Hello, world!")</code>',
        '<pre>This is preformatted text.</pre>', '<meta charset="UTF-8">',
        '<style>body { font-family: Arial; }</style>',
        '<textarea rows="4" cols="50">Enter text here...</textarea>',
        '<abbr title="World Health Organization">WHO</abbr>',
        '<footer>Copyright © 2022 Company Name</footer>',
        '<header>Welcome to our website!</header>',
        '<nav><a href="/">Home</a> <a href="/about">About</a></nav>',
        '<section><h2>Section Title</h2><p>Section content...</p></section>',
        '<aside>Related articles...</aside>',
        '<article><h2>Article Title</h2><p>Article content...</p></article>',
        '<main><h1>Main Content</h1><p>Main content...</p></main>',
        '<time datetime="2022-01-01">January 1, 2022</time>',
        '<address>Contact us at: example@example.com</address>',
        '<hr>', 'This is a line of', '<del>Deleted Text</del>',
        '<ins>Inserted Text</ins>', '<sup>Superscript</sup>', '<sub>Subscript</sub>',
        '<svg><circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" /></svg>',
        '<canvas id="myCanvas" width="200" height="100" style="border:1px solid #000000;"></canvas>'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Write DataFrame to Excel
df.to_excel('html_tags_with_examples.xlsx', index=False)
