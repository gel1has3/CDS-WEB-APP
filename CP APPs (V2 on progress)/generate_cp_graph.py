
import streamlit as st
# import streamlit graph processing module
from streamlit_agraph import agraph, Node, Edge, Config


def generate_cp_graph(selected_rows, *args):
    nodes = []
    edges = []
    # includes **kwargs
    sourceNode = st.multiselect("Nodes:", selected_rows.columns)

    for i, r in selected_rows.head().iterrows():
        nodes.append(Node(id=r['Finding'], size=400))
        nodes.append(Node(id=r['Generated_CP'], size=400))
        edges.append(Edge(source=r['Finding'], target=r['Generated_CP'],
                          weight=r['Generated_CP_Freq']))
        for col in sourceNode:
            nodes.append(Node(id=r[col], label=col, size=400))
            edges.append(Edge(source=r[col], target=r['Urgent_Attention'],
                              weight=r['Generated_CP_Freq']))

    config = Config(width=500,
                    height=500,
                    directed=True,
                    nodeHighlightBehavior=True,
                    highlightColor="blue",  # or "blue"
                    collapsible=True,
                    node={'labelProperty': 'label'},
                    link={'labelProperty': 'label', 'renderLabel': True}
                    # **kwargs e.g. node_size=1000 or node_color="blue"
                    )

    return_value = agraph(nodes=nodes, edges=edges, config=config)

    return return_value
