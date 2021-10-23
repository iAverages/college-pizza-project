import json
import os
from json.decoder import JSONDecodeError 

class Utils:

    @staticmethod
    def getIntInput(message):
        try:
            while True:
                try:
                    res = int(input(message + ": "))
                    return res
                except KeyboardInterrupt:
                    raise KeyboardInterrupt;
                except:
                    print("That is not a number!")
        except KeyboardInterrupt:
            Utils.handleKeyboardInterrupt()

    @staticmethod
    def getStringInput(message):
        try:
            while True:
                res = input(message + ": ")
                if res == "":
                    print("You entered nothing. Make sure you enter a value!")
                else:
                    break
            return res
        except KeyboardInterrupt:
            Utils.handleKeyboardInterrupt()

    acceptYesInput = ["yes", "1", "yea"]

    @staticmethod
    def getYesNoInput(message):
        try:
            while True:
                res = input(message + ": ")
                if res == "":
                    print("You entered nothing. Make sure you enter a value!")
                    continue
                return Utils.acceptYesInput.__contains__(res)
        except KeyboardInterrupt:
            Utils.handleKeyboardInterrupt()

    @staticmethod
    def appendToFile(fileName, data):
        with open(Utils.DATADIR + fileName, "a") as file:
            file.write(data + "\n")

    @staticmethod
    def handleKeyboardInterrupt():
        print("\nKeyboardInterrupt (Ctrl + C). Closing program...")
        exit(0)

    @staticmethod
    def readJSON(filename):
        with open(filename, 'r') as file:
            data = file.read()
            try :
                return json.loads(data)
            except JSONDecodeError:
                return json.loads("{}")

    @staticmethod
    def appendJSONFile(filename, toAppend, lastCallFailed = False):
        try:
            with open(filename, "r+") as file:
                # read, seek to start, delete contents
                data = file.read()
                file.seek(0)
                file.truncate()
                if data == "":
                    print("no json data in file.")
                    data = "[]"
                
                jsonData = json.loads(data)
                jsonData.append(toAppend)

                file.write(json.dumps(jsonData, indent=4))

        except JSONDecodeError:
            print("Invalid JSON was passed to appendJSONFile.")
            exit()
            
        except FileNotFoundError:
            if lastCallFailed:
                print(f"An error occured while saving {filename}. Quiting program.")
                exit()
            try:
                ## Get dir path in filename and create it
                path = os.path.dirname(os.path.abspath(filename));
                if not os.path.exists(path):
                    os.mkdir(path)
                with open(filename, "w") as f:
                    f.write("[]")
            except FileNotFoundError:
                pass
            return Utils.appendJSONFile(filename, toAppend, True)