function getBerry (id){
    for (var id =1; id <=20; ++id) {
        fetch(`https://pokeapi.co/api/v2/berry/${id}`)
    .then(function (response) {
        response.json()
        .then(function(berry) {
            var aBerry = (berry.name)
            let li = document.createElement('li');
            li.textContent = aBerry;
            const list = document.querySelector('#prompt-5 ol');
            list.appendChild(li);
        });
    });
};
};
getBerry();