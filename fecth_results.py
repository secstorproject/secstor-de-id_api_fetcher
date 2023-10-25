import getopt
import sys
from src.run import run

def main():
    options = "ha:t:p:u:"
    try:
        arguments, values = getopt.getopt(sys.argv[1:], options)
        archive = False
        threads = False
        payload = False
        url = False

        for currentArgument, currentValue in arguments:
            if currentArgument == "-h":
                print_help()
            elif currentArgument == "-a":
                archive = currentValue
            elif currentArgument == "-t":
                threads = currentValue
            elif currentArgument == "-p":
                payload = currentValue
            elif currentArgument == "-u":
                url = currentValue

        if archive:
            if threads:
                if payload:
                    if url:
                        run(archive, threads, payload, url)
                    else:
                        print("Need url")
                else:
                    print("Need payload")
            else:
                print("Need threads")
        else:
            print("Need archive")

    except getopt.error as err:
        print(str(err))

def print_help():
    print("""python main.py -h <= Help
           -a <Str:Archive> <= Input Database File (JSON extension)
           -t <Int:Threads> <= Number of Threads
           -p <Int:Payload> <= Payload Configuration
           -u <Int:URL> <= URL Configuration""")

if __name__ == "__main__":
    main()
