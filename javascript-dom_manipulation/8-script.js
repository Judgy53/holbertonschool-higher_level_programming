// Fetch Hello API and display result in #hello
function fetchAndDisplayHello () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    // Convert response to json if ok
    .then((response) => {
      if (!response.ok) {
        throw new Error('Error while fetching hello message');
      }

      return response.json();
    })
    // Display translated hello in #Hello
    .then((json) => {
      document.querySelector('#hello').innerHTML = json.hello;
    })
    // Catch any errors and display them in console
    .catch((error) => {
      console.error(error);
    });
}

// Wait until page is fully loaded to do anything
document.addEventListener('DOMContentLoaded', fetchAndDisplayHello);
