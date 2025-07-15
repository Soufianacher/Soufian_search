import streamlit as st
import pandas as pd

# 🎨 Page settings
st.set_page_config(page_title="Soufian Search", layout="centered")

# 🏷️ Page title (with emoji inside HTML safely)
st.markdown(
    "<h1 style='text-align: center; color: #2b67f6;'>🔍 Soufian Search - Excel Product Finder</h1>",
    unsafe_allow_html=True
)

# 📁 Upload Excel file
uploaded_file = st.file_uploader("📁 Upload Your Product Excel File", type=["xlsx", "xls"])

# 🧠 Function to search in all columns
def search_dataframe(df, query):
    query = str(query).lower()
    mask = df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)
    return df[mask]

# ℹ️ Search instructions
st.info("Type anything like a product code, name, word, or price. It will search in all columns.")

# 🔍 If file is uploaded
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        # ✅ Make sure the required columns are present
        required_cols = ["CODE CAISSE", "DESCRIPTION_ARTICLE", "RAYON", "STOCK_en_QTE", "PRIX_vent"]
        if all(col in df.columns for col in required_cols):

            # 📦 Show search input
            search_input = st.text_input("🔎 Type to search (e.g. cat, 777, bread)...")

            if search_input:
                result_df = search_dataframe(df, search_input)
                st.success(f"✅ Found {len(result_df)} result(s):")

                # 📊 Show results table
                st.dataframe(
                    result_df.style.set_properties(**{
                        'background-color': '#f9fcff',
                        'border-color': 'gray',
                    }),
                    use_container_width=True
                )
        else:
            st.error(f"❌ Your file must have these columns: {', '.join(required_cols)}")

    except Exception as e:
        st.error(f"❌ Could not read the file: {e}")
else:
    st.warning("⬆️ Please upload your Excel file to begin searching.")

# 👣 Footer
st.markdown(
    "<hr><p style='text-align: center; color: gray;'>Made with ❤️ by Soufian</p>",
    unsafe_allow_html=True
)