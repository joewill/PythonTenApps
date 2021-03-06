import os


def load(name):
    """
    creates and loads a new or existing journal

    :param name: the name of the journal
    :return: A new journal data structure
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', '4_journal', 'journals', name + '.jrl'))
    return filename

def save(name, journal_data):
    filename = get_full_pathname(name)
    print("....saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def add_entry(text, journal_data):
    journal_data.append(text)