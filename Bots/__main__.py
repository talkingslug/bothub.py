# importing modules
from io import StringIO
from markdown import Markdown

def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()

# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False

def unmark(text):
    return __md.convert(text)

MD = """
# bothub.py
**Bothub.py** is a Python package used to simplify the creation of bots as scripts.

Currently, you can create bots with Scratchconnect or Selenium. While Selenium is a simpler module, it has a lot of useful functions and, of course, Scratchconnect offers a great way for scripts to interact with Scratch via commands. 

We hope to add a Twilio Voice interface soon as well as a SMS protocol.
"""
print(f"""
 ~~~  BOTHUB.PY  ~~~
 {unmark(MD)}
""")