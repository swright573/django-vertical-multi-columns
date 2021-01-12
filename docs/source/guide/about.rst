==================================
About Django-virtual-multi-columns
==================================

Django-Vertical-Multi-Columns (VMC) is a reusable Django application allowing users to display a list of items in side-by-side columns rather than in one long list.

In a typical "list" view where you are potentially displaying a lot of choices, you might sort them into some logical order (e.g. alphabetical) and display them in one long list on a web page. Django makes it quite easy to do this.

It is quite natural for people to scan their eyes up and down a vertical list to find what they are looking for. But if the list is long, it can be quite annoying to have to do a lot of scrolling or paging up and down.

Django-virtual-multi-columns (VMC) solves the excessive scrolling/paging problem. It enables a view class to generate input to your template that lets you easily display your items in side-by-side columns that are still sorted vertically.

|example|

Some scrolling or paging may still be required but it will be less. The more columns you can display on the page, the less scrolling or paging will be required.

.. |example| image:: https://user-images.githubusercontent.com/31971607/104324478-7e514080-54b5-11eb-9399-da702969429f.GIF
    :alt: Example