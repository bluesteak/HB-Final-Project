fetch('https://api.themoviedb.org/3/person/1663195-kelly-marie-tran?api_key=ca04f28350cde67bc24470dfe961b3dd&language=en-US')
  .then(response => response.json())
  .then(data => console.log(data));