options(
    setup = Bunch(
        name = "pyshapefile",
        packages = ['pyshapefile'],
        version = "0.1",
        author = "Zach Steindler",
        author_email = "steiza@gmail.com",
        description = "Library for loading and visualizing GPS shapefiles"
    )
)

@task
@needs(['generate_setup', 'minilib', 'setuptools.command.sdist'])
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass
