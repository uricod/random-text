from randomText import RandomTextClient


def main():
    client = RandomTextClient()
    response = client.coffee.get_random(size=5)
    print(response)


if __name__ == '__main__':
    main()