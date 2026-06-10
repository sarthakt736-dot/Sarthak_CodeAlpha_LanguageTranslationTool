from deep_translator import GoogleTranslator
import gradio as gr

# All supported languages
LANGUAGES = {
    "Afrikaans (af)": "af", "Albanian (sq)": "sq", "Arabic (ar)": "ar",
    "Bengali (bn)": "bn", "Chinese Simplified (zh-CN)": "zh-CN",
    "Chinese Traditional (zh-TW)": "zh-TW", "Dutch (nl)": "nl",
    "English (en)": "en", "French (fr)": "fr", "German (de)": "de",
    "Gujarati (gu)": "gu", "Hindi (hi)": "hi", "Italian (it)": "it",
    "Japanese (ja)": "ja", "Kannada (kn)": "kn", "Korean (ko)": "ko",
    "Malay (ms)": "ms", "Marathi (mr)": "mr", "Nepali (ne)": "ne",
    "Odia (or)": "or", "Pashto (ps)": "ps", "Persian (fa)": "fa",
    "Polish (pl)": "pl", "Portuguese (pt)": "pt", "Punjabi (pa)": "pa",
    "Romanian (ro)": "ro", "Russian (ru)": "ru", "Sanskrit (sa)": "sa",
    "Sindhi (sd)": "sd", "Sinhala (si)": "si", "Spanish (es)": "es",
    "Swahili (sw)": "sw", "Tamil (ta)": "ta", "Telugu (te)": "te",
    "Thai (th)": "th", "Turkish (tr)": "tr", "Ukrainian (uk)": "uk",
    "Urdu (ur)": "ur", "Vietnamese (vi)": "vi",
}

language_options = list(LANGUAGES.keys())

def translate_text(text, source_lang_str, target_lang_str):
    if not text.strip():
        return "⚠️ Please enter some text to translate."
    try:
        source_code = LANGUAGES[source_lang_str]
        target_code = LANGUAGES[target_lang_str]
        result = GoogleTranslator(source=source_code, target=target_code).translate(text)
        return result
    except Exception as e:
        return f"❌ Translation failed: {str(e)}"

with gr.Blocks(title="🌐 Language Translator — CodeAlpha") as app:
    gr.Markdown("# 🌐 Language Translation Tool")
    gr.Markdown("### CodeAlpha AI Internship | Sarthak Tiwari")
    gr.Markdown("Translate text between 35+ languages instantly.")

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="📝 Enter Text", placeholder="Type something here...", lines=5)
            source_lang = gr.Dropdown(choices=language_options, value="English (en)", label="🔤 Source Language")
            target_lang = gr.Dropdown(choices=language_options, value="Hindi (hi)", label="🎯 Target Language")
            translate_btn = gr.Button("🚀 Translate", variant="primary")
        with gr.Column():
            output_text = gr.Textbox(label="✅ Translated Text", lines=5, interactive=False)

    translate_btn.click(fn=translate_text, inputs=[input_text, source_lang, target_lang], outputs=output_text)

    gr.Examples(
        examples=[
            ["Hello, how are you?", "English (en)", "Hindi (hi)"],
            ["Artificial Intelligence is the future.", "English (en)", "French (fr)"],
            ["मैं ठीक हूँ।", "Hindi (hi)", "Spanish (es)"],
        ],
        inputs=[input_text, source_lang, target_lang]
    )

app.launch()