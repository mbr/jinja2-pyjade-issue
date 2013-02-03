## Just a jinja2-pyjade issue demo

### Demo Steps

1. `mkvirtualenv jinja2-pyjade-issue`
2. `pip install -r requirements.txt`
3. `./myapp.py`
4. Open `http://127.0.0.1:5000/` in your browser.

Now you will find the `<p>OOPS_IN_LAYOUT</p>` was escaped, which not expected.
