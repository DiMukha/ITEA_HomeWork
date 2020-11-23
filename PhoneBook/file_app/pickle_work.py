import pickle


def load():
    try:
        with open(f'data.pickle', 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        data = {}
    return data


def save(data):
    with open(f'data.pickle', 'wb') as f:
        pickle.dump(data.__dict__['_d'], f)
