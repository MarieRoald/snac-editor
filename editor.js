// Setting up the CodeMirror editor
var editor = CodeMirror(document.querySelector('#editor'), {
    lineNumbers: true,
    value: 'print("Hello, world!")',
    mode: 'python'
  });
  
  // Function to download the code as a file
  function saveCodeAs() {
      if (promptFilename = prompt("Save code as", "")) {
          var textBlob = new Blob([editor.getValue()], {type:'text/plain'});
          var downloadLink = document.createElement("a");
          downloadLink.download = promptFilename;
          downloadLink.innerHTML = "Download File";
          downloadLink.href = window.URL.createObjectURL(textBlob);
          downloadLink.click();
      delete downloadLink;
      delete textBlob;
      }
  }
  
  document.getElementById("downloadLink").onclick = saveCodeAs;
  