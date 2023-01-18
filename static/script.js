// Get a reference to the button and text box
var plot = document.getElementById('plot');
var reset = document.getElementById('reset');
var textbox = document.getElementById('textbox');
var spinner = document.getElementById('spinner');

function showSpinner() {
    spinner.style.display = 'block';
}

function hideSpinner() {
    spinner.style.display = 'none';
}


// Add a click event listener to the button
plot.addEventListener('click', function() {
  // Get the value of the text box
  var text = textbox.value;
  showSpinner()
  // Send a POST request to the server with the text as the body
  fetch('/plot', {
    method: 'POST',
    body: text
  }).then(function(response) {
    // When the server responds, update the iframe with the response
    var html = response.text();
    return html;
  }).then(function(responseText) {
    targetFile = responseText;
    hideSpinner()
    var iframe = document.getElementById('iframe');
    // iframe.src = 'data:text/html;charset=utf-8,' + encodeURIComponent(responseText);
    iframe.src = "/"+targetFile;
  });
});

reset.addEventListener('click', function() {
  // Send a POST request to the server with the text as the body
  fetch('/reset', {
    method: 'POST',
  });
});