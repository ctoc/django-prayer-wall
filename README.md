====
prayer-wall
=====

prayer-wall is a Django app to conduct prayer wall.
Visitors post pray request and can pray for others.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "prayer-wall" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'prayer-wall',
    )

2. Include the prayer-wall URLconf in your project urls.py like this::

    url(r'^prayer-wall/', include('prayer-wall.urls')),

3. Run `python manage.py migrate` to create the prayer-wall models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a prayer-wall (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/prayer-wall/ to participate in the prayer-wall.