import configparser

fileName = 'config.ini'
conf = configparser.ConfigParser()


def write():

    f = open(fileName, "w", encoding="utf-8")

    s_name = 'config'
    conf.add_section(s_name)
    a_list = ['model', 'coordinates']
    b_list = ['1', '0, 0, 800, 480']
    for i, j in zip(a_list, b_list):
        conf.set(section=s_name, option=i, value=j)

    conf.write(f)
    f.close()


def model():
    conf.read(fileName, encoding="utf-8")
    sections = conf.sections()
    item = conf.items(sections[0])
    data = item[0][1]
    try:
        text = int(data)
    except:
        text = 0
    return text


def coordinates():
    conf.read(fileName, encoding="utf-8")
    sections = conf.sections()
    item = conf.items(sections[0])
    data = item[1][1].replace(' ', '').split(',')
    try:
        text = [int(i) for i in data]
    except:
        text = [0, 0, 0, 0]
    return text
