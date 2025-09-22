from langgraph.graph import StateGraph,START,END
from src.langgraph_agentic_ai.state.state import State
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BaiscChatbotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using langgraph.
        This method initializes a chatbot node using 'BaiscChatbotNode' class
        and intigrates it into the graph. The chatbot node is set as both the
        entry and exit point of the graph.
        """
        self.basic_chatbot_node = BaiscChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
    
    def setup_graph(self,usecase:str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()