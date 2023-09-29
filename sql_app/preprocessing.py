def preprocess_text(text):
    # 簡単なテキストの前処理の例
    return text.str.lower().str.replace('[^\w\s]', '')