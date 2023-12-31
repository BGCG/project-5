import streamlit as st


# Class to create multiple Streamlit pages and run method to navigate between them
class Multipage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
           page_title=self.app_name,
           page_icon=":seedling:")
        # short code for page icon from https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
