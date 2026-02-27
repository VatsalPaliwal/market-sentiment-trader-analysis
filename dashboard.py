import streamlit as st
st.set_page_config(page_title="Market Sentiment & Trader Behavior Dashboard", layout="wide")

import pandas as pd
import plotly.express as px

performance =pd.read_csv("data/derived/performance_by_sentiment.csv")
behavior = pd.read_csv("data/derived/behavior_by_sentiment.csv")
activity_seg = pd.read_csv("data/derived/activity_segmentation.csv")
volatility_seg = pd.read_csv("data/derived/volatility_segmentation.csv")

st.title("Market Sentiment & Trader Behavior Dashboard")

section = st.sidebar.radio(
    "Select Section",
    ["Performance Analysis", "Behavior Analysis", "Segmentation Analysis"]
)
if section == "Performance Analysis":

    st.subheader("Performance by Sentiment")

    # KPI Row
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Highest Median PnL",
        performance.loc[performance['median_pnl'].idxmax(), 'classification']
    )

    col2.metric(
        "Highest Win Rate",
        performance.loc[performance['avg_win_rate'].idxmax(), 'classification']
    )

    col3.metric(
        "Highest Volatility",
        performance.loc[performance['pnl_volatility'].idxmax(), 'classification']
    )

    col4.metric(
        "Worst Downside Regime",
        performance.loc[performance['worst_day'].idxmin(), 'classification']
    )

    st.markdown("---")

    # Side-by-side charts
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            performance,
            x="classification",
            y="median_pnl",
            title="Median Daily PnL",
            text_auto=True
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.bar(
            performance,
            x="classification",
            y="pnl_volatility",
            title="PnL Volatility",
            text_auto=True
        )
        st.plotly_chart(fig2, use_container_width=True)


elif section == "Behavior Analysis":

    st.subheader("Behavior by Sentiment")

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            behavior,
            x="classification",
            y="avg_trades",
            title="Average Trades per Day",
            text_auto=True
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.bar(
            behavior,
            x="classification",
            y="avg_trades",
            title="Average Trade Size",
            text_auto=True
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Behavior Summary Table")
    st.dataframe(behavior)

elif section == "Segmentation Analysis":
    st.subheader("Segmentation Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.bar(
            activity_seg,
            x="classification",
            y="daily_pnl",   # change to "median_pnl" if that is your actual column
            color="activity_segment",
            barmode="group",
            title="Median PnL by Activity Segment",
        )
    
        fig1.update_traces(opacity=1)  # remove transparency
        fig1.update_layout(
            yaxis_showgrid=False,
            xaxis_showgrid=False,
            plot_bgcolor="rgba(0,0,0,0)"
        )
    
        st.plotly_chart(fig1, use_container_width=True)
    
    
    with col2:
        fig2 = px.bar(
            volatility_seg,
            x="classification",
            y="daily_pnl",   # change to "median_pnl" if needed
            color="volatility_segment",
            barmode="group",
            title="Median PnL by Volatility Segment",
        )
    
        fig2.update_traces(opacity=1)
        fig2.update_layout(
            yaxis_showgrid=False,
            xaxis_showgrid=False,
            plot_bgcolor="rgba(0,0,0,0)"
        )
    
        st.plotly_chart(fig2, use_container_width=True)