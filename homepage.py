import math
import streamlit as st
from urllib.parse import urlencode

from db import list_chats, create_chat, update_chat, delete_chat, read_chat


def chats_page():
    st.markdown(
        "<h1 style='text-align: center;'>StudySage🧙‍♂️</h1>", unsafe_allow_html=True
    )

    with st.container(border=True):
        col1, col2 = st.columns([0.8, 0.2])

        with col1:
            chat_title = st.text_input(
                "Chat Title", placeholder="Enter Chat Title", key="chat_title"
            )

        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Add vertical space
            if st.button("Create Chat", type="primary"):
                if chat_title:
                    chat_id = create_chat(chat_title)
                    st.success(f"Created new chat: {chat_title}")
                    st.query_params.from_dict({"chat_id": chat_id})
                    st.rerun()
                else:
                    st.warning("Please enter a chat title")

    with st.container(border=True):
        st.subheader("Previous Chats")

        # get previous chats from db
        previous_chats = list_chats()

        # Pagination settings
        chats_per_page = 5
        total_pages = math.ceil(len(previous_chats) / chats_per_page)

        # Get current page from session state
        if "current_page" not in st.session_state:
            st.session_state.current_page = 1

        # Calculate start and end indices for the current page
        start_idx = (st.session_state.current_page - 1) * chats_per_page
        end_idx = start_idx + chats_per_page

        # Display chats for the current page
        for chat in previous_chats[start_idx:end_idx]:
            chat_id, chat_title = chat[0], chat[1]
            with st.container(border=True):
                col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
                with col1:
                    st.write(chat_title)
                with col2:
                    if st.button("Open", key=f"open_{chat_id}"):
                        st.query_params.from_dict({"chat_id": chat_id})
                        st.rerun()
                with col3:
                    if st.button("Delete", key=f"delete_{chat_id}"):
                        delete_chat(chat_id)
                        st.success(f"Deleted chat: {chat_title}")
                        st.rerun()

        # Pagination controls
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("Previous") and st.session_state.current_page > 1:
                st.session_state.current_page -= 1
                st.rerun()
        with col2:
            st.write(f"Page {st.session_state.current_page} of {total_pages}")
        with col3:
            if st.button("Next") and st.session_state.current_page < total_pages:
                st.session_state.current_page += 1
                st.rerun()


def chat_page(chat_id):
    chat = read_chat(chat_id)  # You'll need to implement this function
    if not chat:
        st.error("Chat not found")
        return

    st.markdown(
        "<h1 style='text-align: center;'>StudySage🧙‍♂️</h1>", unsafe_allow_html=True
    )
    st.subheader(f"Chat: {chat[1]}")  # Assuming chat[1] is the title

    # Here you would typically load and display the chat history

    # Add a text input for new messages
    prompt = st.chat_input("Say something")
    if st.button("Send"):
        if prompt:
            # Here you would typically save the new message to your database
            st.success(f"Sent message: {prompt}")
        else:
            st.warning("Please enter a message")

    # Add a button to return to the main chats page
    if st.button("Back to Chats"):
        st.query_params.clear()
        st.rerun()


def main():
    query_params = st.query_params
    if "chat_id" in query_params:
        chat_id = query_params["chat_id"][0]
        chat_page(chat_id)
    else:
        chats_page()


if __name__ == "__main__":
    main()
