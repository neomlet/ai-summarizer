from core.preprocess import clean_text, split_paragraphs

def test_clean_text():
    dirty_text = "<p>Hello   world! &amp; </p>"
    cleaned = clean_text(dirty_text)
    assert cleaned == "Hello world! &"

def test_split_paragraphs():
    text = "First sentence. Second sentence? Third"
    paragraphs = split_paragraphs(text)
    assert len(paragraphs) == 2
    assert paragraphs[0] == "First sentence."
    assert paragraphs[1] == "Second sentence? Third"