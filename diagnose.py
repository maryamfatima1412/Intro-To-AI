import traceback
import sys

print("Step 1: Python version:", sys.version)

try:
    print("Step 2: importing tkinter...")
    import tkinter as tk
    print("   OK - tkinter imported")

    print("Step 3: importing wordle_game...")
    import wordle_game
    print("   OK - wordle_game imported")
    print("   WORDS_FILE points to:", wordle_game.WORDS_FILE)
    import os
    print("   Does that file exist?", os.path.exists(wordle_game.WORDS_FILE))

    print("Step 4: importing wordle_gui...")
    import wordle_gui
    print("   OK - wordle_gui imported")

    print("Step 5: creating Tk root window...")
    root = tk.Tk()
    print("   OK - root created")

    print("Step 6: creating WordleApp...")
    app = wordle_gui.WordleApp(root)
    print("   OK - WordleApp created, word list size:", len(app.word_list))

    print("Step 7: entering mainloop (window should appear now)...")
    root.mainloop()
    print("Step 8: mainloop exited normally (you closed the window)")

except Exception:
    print("\n*** AN ERROR HAPPENED - full details below ***\n")
    traceback.print_exc()

input("\nPress Enter to close this window...")
