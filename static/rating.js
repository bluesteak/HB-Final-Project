
document.querySelector('#favorite-button').addEventListener('submit', () => {
  const form = document.querySelector('#add-favorite-movie form');
  const button = form.querySelector('button');
  var userInput = document.querySelector('#favorite-button').value();
  alert(userInput);


});