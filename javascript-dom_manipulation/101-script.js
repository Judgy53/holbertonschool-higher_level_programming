// Fetch hello API for specific language and display the result in outputElem
function fetchAndDisplayHello (langSelectElem, outputElem) {
  const langCode = langSelectElem.value;

  // Make sure a language is actually selected before trying to fetch
  if (!langCode || langCode.length <= 0) {
    console.error('No language Selected. Please Select a language.');
    return;
  }

  // fetch the api with the selected language
  fetch('https://hellosalut.stefanbohacek.dev/?lang=' + langCode)
    // Convert the response to json if ok
    .then((response) => {
      if (!response.ok) {
        throw new Error('Error while fetching hello message');
      }

      return response.json();
    })
    // Display the result in #hello
    .then((json) => {
      outputElem.innerHTML = json.hello;
    })
    // Catch any error and display it in the console
    .catch((error) => {
      console.error(error);
    });
}

// Add click event to #btn_translate
function onPageLoaded () {
  const outputElem = document.querySelector('#hello');
  const langSelectElem = document.querySelector('#language_code');

  document.querySelector('#btn_translate').addEventListener('click', () => fetchAndDisplayHello(langSelectElem, outputElem));
}

// Wait until page is fully loaded to do anything
document.addEventListener('DOMContentLoaded', onPageLoaded);
