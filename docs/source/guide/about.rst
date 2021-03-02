*****
About
*****

Django-Vertical-Multi-Columns (VMC) is a reusable Django application allowing users to display a list of items in vertically sorted side-by-side columns rather than in one long list.

In a typical "list" view where you need to display many choices, you would likely sort them into some logical order (e.g. alphabetical) and display them in one long vertical list on a web page. Django makes it quite easy to do this.

Scanning up and down a vertical list to find something is quite natural for people. But if the list is long, it can be quite annoying to be forced to do a lot of scrolling or paging up and down to find what you want.

Django-virtual-multi-columns (VMC) solves that excessive scrolling/paging problem. It enables a view class to generate input to your template so you can easily display your items in side-by-side columns that are still sorted vertically.

|example|

Even if there are a lot of choices and some scrolling or paging is still required, there will be less of it. The more columns you can display on the page, the less scrolling or paging there will be.

.. |example| image:: https://user-images.githubusercontent.com/31971607/104324478-7e514080-54b5-11eb-9399-da702969429f.GIF
    :alt: Example
