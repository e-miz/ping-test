# %%
import pandas as pd
import plotly.express as px
# %%
input_file = "2024-09-01-0.csv"
# %%
df = pd.read_csv(input_file)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

# %%
df["missed_packets"] = (df.diff()["icmp_seq"].fillna(1) - 1).astype("category")

# %%
fig = px.line(
    df, x="timestamp", y="time_ms", labels={"time_ms": "Ping [ms]", "timestamp": "Date"}
)
fig.add_traces(
    px.scatter(
        df,
        x="timestamp",
        y="time_ms",
        title="ping",
        color="missed_packets",
        category_orders={"missed_packets": df.missed_packets.unique().sort_values()},
    ).data
)
fig.update_layout(legend_title_text="Packets Missed")

# %%
px.histogram(df, x="time_ms")
# %%
