"""
File without any web framework - should not detect any patterns
"""


def main():
    data = load_data()
    processed = process(data)
    save_results(processed)


def load_data():
    with open('data.json') as f:
        return parse_json(f.read())


def process(data):
    filtered = filter_data(data)
    transformed = transform(filtered)
    return transformed


def save_results(data):
    write_to_file(data)
    print("Done")


def parse_json(text):
    return {}


def filter_data(data):
    return data


def transform(data):
    return data


def write_to_file(data):
    pass


class DataProcessor:
    def __init__(self, config):
        self.config = config

    def run(self):
        self.load()
        self.process()
        self.save()

    def load(self):
        pass

    def process(self):
        pass

    def save(self):
        pass


if __name__ == '__main__':
    main()
