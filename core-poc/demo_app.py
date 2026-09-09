import streamlit as st
import numpy as np
from optimizer import QuantumRouteOptimizer

st.set_page_config(page_title="LogisticQ Live Demo", page_icon="🚚", layout="centered")

st.title("🚚 LogisticQ: Quantum-Ready Route Optimizer")
st.write("Welcome to the live demonstration of the open-source hybrid quantum logistics engine.")

st.sidebar.header("🎛️ Simulation Parameters")
nodes_count = st.sidebar.slider("Number of Delivery Nodes", min_value=3, max_value=5, value=3)

st.subheader("📍 1. Define Distance Matrix (KM)")
st.write("Simulating coordinate weights between your Warehouse (Node 0) and Clients.")

# Generate sample matrix dynamically based on slider
if nodes_count == 3:
    matrix = [[0, 10, 15], [10, 0, 35], [15, 35, 0]]
elif nodes_count == 4:
    matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
else:
    matrix = [[0, 10, 15, 20, 25], [10, 0, 35, 25, 18], [15, 35, 0, 30, 22], [20, 25, 30, 0, 12], [25, 18, 22, 12, 0]]

st.matrix = st.data_editor(matrix)

st.subheader("🔮 2. Execute Hybrid Optimization")
if st.button("🚀 Run Quantum Optimization Pipeline"):
    with st.spinner("Formulating QUBO and dispatching to solver..."):
        optimizer = QuantumRouteOptimizer(nodes=nodes_count)
        optimizer.set_distance_matrix(matrix)
        qubo = optimizer.formulate_qubo()
        
        # Fallback to classical for open-source high-accessibility preview
        best_route = optimizer.solve_classical_fallback()
        
    st.success("Optimization Complete!")
    
    # Format the route string nicely
    route_str = " -> ".join([f"Node {i}" for i in best_route])
    
    st.metric(label="Optimal Supply Chain Path", value=route_str)
    st.info("💡 Note: This demo currently runs in High-Accessibility Fallback Mode (Simulated QUBO). In production, this data streams directly via D-Wave Leap or AWS Braket API hooks.")
