import os
from doit.action import CmdAction


GEOFABRIK_DATA_URL = 'http://download.geofabrik.de/south-america-latest.osm.pbf'
OUTPUT_DIR = './'
INPUT_DIR = OUTPUT_DIR


def task_download_osmconvert():
    def wget_cmd():
        return 'wget -O data/osmconvert.c http://m.m.i24.cc/osmconvert.c'

    return {
        'actions': [CmdAction(wget_cmd)],
        'file_dep': [],
        'targets': ['data/osmconvert.c'],
        'uptodate': [None],  # TODO: check with the server filesize or something
    }


def task_compile_osmconvert():
    def cc_cmd():
        return 'cc -x c %(dependencies)s -lz -O3 -o osmconvert'

    return {
        'actions': [CmdAction(cc_cmd)],
        'file_dep': ['data/osmconvert.c'],
        'targets': ['bin/osmconvert'],
        'uptodate': [None],  # TODO: check with the server filesize or something
    }


def task_download_paraguay_poly():
    def wget_cmd():
        return 'wget "http://polygons.openstreetmap.fr/get_poly.py?id=287077&params=0" -O data/paraguay.poly'

    return {
        'actions': ['rm -f data/paraguay.poly', CmdAction(wget_cmd)],
        'file_dep': [],
        'targets': ['data/paraguay.poly'],
        'uptodate': [None],  # TODO: check with the server filesize or something
    }


def task_download_data():
    def wget_cmd():
        return 'wget -c ' + GEOFABRIK_DATA_URL + ' -O %(targets)s'

    return {
        'actions': [CmdAction(wget_cmd)],
        'file_dep': [],
        'targets': [os.path.join(INPUT_DIR, 'data/south-america-latest.osm.pbf')],
        'uptodate': [False],  # TODO: check with the server filesize or something
    }


def task_crop_data():
    def osmconvert_cmd():
        input_file = os.path.join(INPUT_DIR, 'data/south-america-latest.osm.pbf')
        poly_file = 'data/paraguay.poly'
        return 'bin/osmconvert ' + input_file.replace(' ', '\ ')  + ' -B=' + poly_file + ' -o=%(targets)s'

    return {
        'actions': [CmdAction(osmconvert_cmd)],
        'file_dep': [
            'bin/osmconvert',
            os.path.join(OUTPUT_DIR, 'data/south-america-latest.osm.pbf'),
            'data/paraguay.poly'],
        'targets': [os.path.join(OUTPUT_DIR, 'data/south-america-paraguay.osm.pbf').replace(' ', '\ ')],
        # 'uptodate': [None],  # TODO: check the file timestamp
    }
