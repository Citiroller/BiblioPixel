from .. util import log

DEFAULT_PROJECT = {
    'animation': {},
    'driver': {},
    'drivers': [],
    'layout': {},
    'maker': 'bibliopixel.project.data_maker.Maker',
    'path': '',
    'run': {},
    'typename': 'bibliopixel.project.project2.Project',
}


def merge(*projects):
    """
    Merge zero or more dictionaries representing projects with the default
    project dictionary and return the result
    """
    result = {}
    for project in (DEFAULT_PROJECT,) + projects:
        for name, section in (project or {}).items():
            if name in ('drivers', 'path', 'typename'):
                result[name] = section
            else:
                if isinstance(section, str):
                    section = {'typename': section}
                result.setdefault(name, {}).update(section)

    return result
