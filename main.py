import wiktionaryReader
import mirriamReader

def main():

    wiki = wiktionaryReader.witionaryReader()
    wiki.hello_world()

    mirriam = mirriamReader.mirriamReader()
    mirriam.hello_world()

if __name__ == "__main__":

    main()