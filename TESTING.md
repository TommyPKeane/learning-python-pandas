# How to Test the code in this Repo

This document covers the testing of any of the code in this repo, before or after any modifications that you (or I) may make to the source code.

Please be sure that you've reviewed the [`CONTRIBUTING.md`](./CONTRIBUTING.md) file and [`README.md`](./README.md) documents to make sure that you have all the necessary prerequisites installed on your system.

<!-- MarkdownTOC -->

- [What is `pytest`?](#what-is-pytest)
- [Running `pytest`](#running-pytest)
- [Updating `pytest` Unit-Testing](#updating-pytest-unit-testing)
- [References](#references)

<!-- /MarkdownTOC -->

<a id="what-is-pytest"></a>
## What is `pytest`?

This is a Python repository, so to facilitate the testing of the source code we've decided to go with [`pytest`]() as the testing library/framework.

`pytest` follows a complex internal design that's meant to simplify the writing of repeatable and reusable test code, though your interpretation of that goal being achieved could be debatable.

With `pytest`, the concept of a "Test Fixture" is borrowed from physical electronics and hardware testing, wherein a factory may have a "test fixture" in which each new "widget" built in the factory can be dropped _into_ the fixture and then tested against it, to remove variability and enforce consistency in the testing.

Personally, with a background in Electrical Engineering and having worked with actual physical, electronic test fixtures, this concept has long made sense to me, but it may not be familiar to everyone.

To add complication though, whether you're familiar or not, we have the issue of the nature of the actual coding in Python by which we actually pass the _fixtures_ into the test functions, instead of snapping our code into our fixtures and running our tests. Like all things with computers, this ambiguity comes down to your conceptualization of the directionality of the word "in" ... which is absurd ... but it's the world we live _in_ :woman_shrugging:.

So, before I ramble forever, I'll just say that I'd suggest that you please check the reference links in this document and keep in mind this short (but complex) summary:

> `pytest` expects/supports the reusability of Python objects by decorating a function as a `@pytest.fixture()`, then you pass that function alias to any test method that you want to be able to have access to the fixture object. `pytest` handles the re-aliasing _via_ the decorator syntax with the help of the Python interpreter, and the `scope` parameter of the `fixture()` decorator method lets you determine the lifetime of each fixture object.

<a id="running-pytest"></a>
## Running `pytest`

To run all of the unit-tests with their innate configuration as defined by the repository's `pyproject.toml` and `conftest.py` modules (files), you simply need to run the bash command:

```bash
pytest
```

This should take a few seconds to run, and then produce an output showing the "Code Coverage" for the repository in a tabular format like this:

```bash
---------- coverage: platform darwin, python 3.10.7-final-0 ----------
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
pandas_demos/__init__.py                         0      0   100%
pandas_demos/dataframe_examples.py               2      0   100%
pandas_demos/dataframe_groupby_examples.py       0      0   100%
pandas_demos/series_examples.py                  0      0   100%
----------------------------------------------------------------
TOTAL                                            2      0   100%
```

The Code Coverage report basically shows all the source code files that `pytest` and the `pytest-cov` package are aware of (per the `pyproject.toml` configuration), and then presents the amount of the code in each of those modules that is successfully "covered" by a passing unit-test.

Code Coverage is not the be-all/end-all metric for the "reliability" of a repository, but it is a helpful metric. If you have strong code coverage, that _can_ be an indicator of the fact that you have a majority of your code "protected" or "covered" by validation through unit-testing.

That being said; it's actually unfortunately pretty easy to "trick" or "cheat" a Code Coverage metric, and while it should be used, it shouldn't be blindly followed. If you make changes to a repo and that lowers the Code Coverage, then yes, that's a potential signal of a bad change ... but it also may be entirely expected. Code Coverage should be treated in that way as like an "out of bounds" alarm. If the Code Coverage changes in a way you didn't expect, that's a great indicator that you should double-check what you're doing, because clearly your unit-testing isn't aligning with your code.

But the biggest mistake that can be made in Software Engineering is to think that if the Code Coverage is high and all the Unit-Tests are passing, that that means that everything is perfect / fine / works-great. As much as we'd love that to be true, it's not guaranteed. If you have a bunch of trivial unit-tests that leave a lot of logical holes/gaps exposed, then you can get 100% Code Coverage that may really only indicate a 30% assurance that your code is viable and operational to desired specifications/requirements.

That's not an exaggeration; and it could be even worse than that. Unit-Testing goes beyond just _having_ unit-tests, and requires actually reinforcing design constraints and expectations by adequately developing robust testing.

<a id="updating-pytest-unit-testing"></a>
## Updating `pytest` Unit-Testing

All of the Unit-Tests for this repo (per the `pyproject.toml` configuration) are in the `tests_unit/` directory, with a structure that then mirrors the code structure for the entire repository.

All Unit-Test modules should be named in the format: `test_{MODULE}.py` where `{MODULE}` is the name of the source code module (file) with the code to be tested.

For example:

- Source Code: `/pandas_demos/dataframe_examples.py`
- Unit-Tests: `/tests_unit/pandas_demos/test_dataframe_examples.py`

<a id="references"></a>
## References

- https://realpython.com/python-testing/
- https://docs.pytest.org/en/7.2.x/
- https://docs.pytest.org/en/7.2.x/explanation/fixtures.html
- https://docs.pytest.org/en/7.2.x/how-to/parametrize.html
