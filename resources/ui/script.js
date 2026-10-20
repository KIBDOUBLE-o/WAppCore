function showText() {
  const text = document.getElementById("textInput").value;
  //document.getElementById("result").textContent = text;
  window.pywebview.api.call("print", [text]);
}