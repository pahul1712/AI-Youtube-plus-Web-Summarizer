import validators,streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import YoutubeLoader,UnstructuredURLLoader


## Streamlit APP

st.set_page_config(page_title="AI-Youtube-plus-Web-Summarizer",page_icon="📚")



# Custom Styling for Main Section:
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(145deg, #b5d0ff 0%, #e8e3ff 60%, #ffffff 100%) !important;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem 3rem;
            border-radius: 15px;
            box-shadow: 0px 4px 25px rgba(0, 0, 0, 0.1);
        }
        .title {
            text-align: center;
            font-size: 2.3em;
            font-weight: 700;
            color: #004aad;
        }

        .subtitle {
            text-align: center;
            color: #4a4a4a;
            font-size: 1.1em;
            margin-bottom: 25px;
        }
        .stButton>button {
        background: linear-gradient(90deg, #0078d4, #00b4d8);
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #00b4d8, #0078d4);
        }
        .summary-box {
            background-color: #e6f9ff;
            border-left: 5px solid #00b4d8;
        }
    </style>
""", unsafe_allow_html=True)



# Title
st.title("📘 AI-Youtube-plus-Web-Summarizer")
st.subheader("Summarize YouTube videos 🎥 or Web Articles 🌐 using Groq + LangChain in seconds!")



## Sidebar: Get the Groq API key and url(YT or Website) to be summarized
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    groq_api_key = st.text_input("🔑 Enter Groq API Key", value="", type="password")
    st.markdown("---")
    st.markdown("**💡 Tip:** Obtain your Groq API key from [groq.com](https://console.groq.com).")


# Main input 
st.markdown("### 🔗 Enter YouTube or Website URL")
generic_url = st.text_input("Paste URL here 👇", label_visibility="collapsed", placeholder="https://...")




prompt_template = """
Provide a clear, concise summary of the following content in about 300 words.
Content:{text}

"""

prompt=PromptTemplate(template=prompt_template,input_variables=["text"])

# Aligning button at the center
col1, col2, col3 = st.columns([1,2,1])
with col2:
    summarize_btn = st.button("✨ Summarize the Content")


# After pressing button:
if summarize_btn:
    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("❌ Please provide both the API key and a valid URL.")
    elif not validators.url(generic_url):
        st.error("⚠️ Enter a proper URL (e.g., YouTube or website).")

    else:
        try:
            with st.spinner("🧠 Analyzing and summarizing... please wait ⏳"):
                ## loading the website or yt video data
                ## Model using Groq API
                llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=groq_api_key)


                if "youtube.com" in generic_url:
                    # Clean URL parameters like &t=249s, &list=PL...
                    if "&" in generic_url:
                        generic_url = generic_url.split("&")[0]

                    try:
                        loader = YoutubeLoader.from_youtube_url(
                            generic_url, add_video_info=True
                        )
                        docs = loader.load()
                    except Exception as e:
                        st.error(
                            f"Unable to fetch transcript. This video may be private, region-locked, "
                            f"or YouTube API temporarily blocked access.\n\nError details: {e}"
                        )
                        st.stop()
                else:
                    loader = UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                   headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    
                    docs = loader.load()

                ## Chain for Summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary = chain.run(docs)

                st.success("✅ Summary Generated Successfully!")
                st.markdown("---")
                # 🟢 Stylized output box
                st.markdown("### 🧾 Generated Summary ")
                st.markdown(f"<div style='background-color:rgba(255, 255, 255, 0.7);padding:15px;border-radius:10px'>{output_summary}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.exception(f"Exception Occured:{e}")


st.markdown(
    """
    ---
    <div style='text-align:center;font-size:0.9em;color:gray;'>
        Made by Pahuldeep Singh Dhingra using LangChain + Groq API + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)