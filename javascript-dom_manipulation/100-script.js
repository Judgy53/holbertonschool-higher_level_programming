// Create a new li item and append it to listElem
function addItemToList (listElem) {
  const itemElem = document.createElement('li');
  itemElem.innerHTML = 'Item';
  listElem.append(itemElem);
}

// Remove last child from listElem
function removeLastChildFromList (listElem) {
  if (listElem.childElementCount <= 0) return;

  listElem.lastElementChild.remove();
}

// Remove every child from listElem
function clearList (listElem) {
  while (listElem.childElementCount > 0) removeLastChildFromList(listElem);
}

// Add click events on #add_item, #remove_item and #clear_list
function onPageLoaded () {
  const myListElem = document.querySelector('.my_list');

  document.querySelector('#add_item').addEventListener('click', () => addItemToList(myListElem));
  document.querySelector('#remove_item').addEventListener('click', () => removeLastChildFromList(myListElem));
  document.querySelector('#clear_list').addEventListener('click', () => clearList(myListElem));
}

// Wait until page is fully loaded to do anything
document.addEventListener('DOMContentLoaded', onPageLoaded);
