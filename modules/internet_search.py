import webbrowser
import wikipedia

def search_web(query, search_engine='google'):
    if search_engine == 'google':
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif search_engine == 'youtube':
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif search_engine == 'wikipedia':
        result = wikipedia.summary(query, sentences=2)
        print(result)
    else:
        print("Invalid search engine. Please specify 'google', 'youtube', or 'wikipedia'.")
