import webbrowser
import os

def main():
    # путь до index.html
    path = os.path.join(os.path.dirname(__file__), "index.html")
    # открываем в браузере
    webbrowser.open_new_tab(f"file://{path}")

if __name__ == "__main__":
    main()
