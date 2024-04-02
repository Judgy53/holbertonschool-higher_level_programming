function addItemToList (listElem) {
  const itemElem = document.createElement('li');
  itemElem.innerHTML = 'Item';
  listElem.append(itemElem);
}

function removeLastChildFromList (listElem) {
  if (listElem.childElementCount <= 0) return;

  listElem.lastElementChild.remove();
}

function clearList (listElem) {
  while (listElem.childElementCount > 0) removeLastChildFromList(listElem);
}

function onPageLoaded () {
  const myListElem = document.querySelector('.my_list');

  document.querySelector('#add_item').addEventListener('click', () => addItemToList(myListElem));
  document.querySelector('#remove_item').addEventListener('click', () => removeLastChildFromList(myListElem));
  document.querySelector('#clear_list').addEventListener('click', () => clearList(myListElem));
}

document.addEventListener('DOMContentLoaded', onPageLoaded);
