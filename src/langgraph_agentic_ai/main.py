import streamlit as st
from src.langgraph_agentic_ai.ui.streamlit.loadui import LoadStreamlitUI
from src.langgraph_agentic_ai.LLMS.groqllm import Groqllm
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.streamlit.display_result import DisplayResult

def load_langgraph_agentic_app():
    """
    Loads and runs the Langgraph AgenticAI application with streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case and displays the output while
    implementing exception handling for robustness.
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error : Failed to load user input from the UI.")
        return
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = Groqllm(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error : LLM model could not be initialized")
                return
            
            # setting up the graph based on use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error : No use case selected")
            
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResult(usecase,graph,user_message).display_result()
            except Exception as e:
                st.error(f"Error : Graph set up failed - {e}")
                return
        except Exception as e:
            st.error(f"Error: Graph set up failed - {e}")
            return

    