## About

A python library for loading and visualizing GPS shapefiles.

This library is designed to work with large data sets, where you might not
want to load all information at once. A typical usage might look something
like this:

    shp = ShapefileData('path/to/your_shapefile_name_without_extension')

    shp.load_objects()
    shp.dbf_load_objects()

    shp.view_data()

After calling this methods, you can access data like this:

    for each in shp.items.itervalues():
            if item['type'] == 'polyline':
                print each['points']

            print each[<dbf field name>]


## License

This project is licensed under the [MIT License][1]

[1]: http://opensource.org/licenses/MIT

