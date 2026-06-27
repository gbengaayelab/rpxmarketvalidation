from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


def render_app() -> None:
    st.set_page_config(
        page_title="RPX — Market Validation · Investment Decision Dashboard",
        page_icon="R",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Remove Streamlit chrome so the embedded app feels like the original page.
    st.markdown(
        """
        <style>
          html, body {min-height: 100%; overflow-x: hidden; overflow-y: auto;}
          #MainMenu {visibility: hidden;}
          footer {visibility: hidden;}
          header {visibility: hidden;}
          .stMainBlockContainer {padding: 0; margin: 0;}
          .block-container {padding: 0; margin: 0; width: 100%;}
          iframe {display: block; width: 100%; min-height: 100vh; border: none;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    html_path = Path(__file__).with_name("rpx_dashboard.html")
    html = html_path.read_text(encoding="utf-8")
    components.html(html, height=1800, scrolling=True)


if __name__ == "__main__":
    from streamlit.web import bootstrap

    try:
        bootstrap.run(__file__, False, [], {})
    except RuntimeError as exc:
        if "Runtime instance already exists" not in str(exc):
            raise
        render_app()
else:
    render_app()
