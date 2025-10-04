import streamlit as st

# Initialize session state to store bids
if "bids" not in st.session_state:
    st.session_state.bids = {}

st.title("🧑‍💼 Silent Auction Bidding System")

with st.form("bid_form"):
    name = st.text_input("Enter your name:")
    bid = st.number_input("Enter your bid amount ($):", min_value=1, step=1)
    submitted = st.form_submit_button("Submit Bid")

    if submitted and name:
        st.session_state.bids[name] = bid
        st.success(f"Bid submitted for {name}!")

# Show current bids
if st.session_state.bids:
    st.subheader("Current Bids")
    for bidder, amount in st.session_state.bids.items():
        st.write(f"{bidder}: ${amount}")

    if st.button("Finish Bidding and Show Winner"):
        winner = max(st.session_state.bids, key=st.session_state.bids.get)
        highest_bid = st.session_state.bids[winner]
        st.success(f"🏆 The winner is **{winner}** with a bid of **${highest_bid}**!")