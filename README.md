# Technical Test

## Objective

Design a small list application, where each item can be assigned to a category. Keep page counts.

## Decision Rationale

* I didn't include an edit function as it wasn't in the specification, although could have easily been done with an `UpdateView` implementation
* Each item can only belong to one category as per specification
* I decided to use templates for the views rather than developing an API and JavaScript frontend as the test seems specifically aimed at my Python/Django skills
* Middleware was my first choice for the PageView, however on second thoughts I could have tried it as a context processor
* Middleware was implemented with a database model which is inefficient, I would have otherwise considered a cache that is occasionally written to disk for persistence
* Larger/more complex apps would probably involve splitting models out into their own directory and sub-files. Same with views.
* I would use some form of secret management for `SECRET_KEY` in tarot\settings.py