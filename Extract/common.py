import yaml


__config = None


def config():
    global __config

    if not __config:
        with open('config.yaml', 'r') as f:
            __config = yaml.load(f, Loader = yaml.FullLoader)


    return __config
