function showText() {
  const text = document.getElementById("textInput").value;
  window.pywebview.api.call("print", [text]);
}

function setText(new_text) {
    const text = document.getElementById("textInput");
    text.value = new_text;
}