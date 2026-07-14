# download_corpora.py
import nltk
import textblob

def download_all_corpora():
    print("📥 Downloading NLTK corpora...")
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('brown')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('stopwords')
    print("✅ NLTK corpora downloaded")
    
    print("📥 Downloading TextBlob corpora...")
    try:
        # Try different methods
        try:
            from textblob.download_corpora import download_all
            download_all()
        except ImportError:
            try:
                import textblob.download_corpora
                textblob.download_corpora.download_all()
            except AttributeError:
                # If all else fails, download using textblob's internal method
                import textblob
                textblob.download_corpora.download_all()
    except Exception as e:
        print(f"⚠️ TextBlob download error: {e}")
        # Fallback: download just what we need
        nltk.download('brown')
        nltk.download('wordnet')
    
    print("✅ All corpora downloaded successfully!")

if __name__ == "__main__":
    download_all_corpora()
