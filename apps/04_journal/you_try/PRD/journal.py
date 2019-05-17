import os
"""
This is Journal module
"""


def load(name):
    '''
    This method creates and loads a new journal
    :param name: this base name of the journal to load
    :return: a new journal data structure is populated with file data
    '''
    data = []
    filename = get_full_path_name(name)

    if os.path.exists(filename):
        with open(filename, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):
    filename = get_full_path_name(name)
    print('...Saving to: {}'.format(filename))

    # fout = open(filename, 'w')
    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + "\n")

    # fout.close()


def get_full_path_name(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.txt'))

    return filename


def add_entry(text, data):
    data.append(text)

