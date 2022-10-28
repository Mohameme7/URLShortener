const btn = document.getElementById('ere');

console.log(btn);

btn.addEventListener('click', () => {
  var textvalue = document.getElementById("linkarea").value;
  let xhr = new XMLHttpRequest();
  xhr.open("POST", 'http://127.0.0.1:5000/create');
  xhr.setRequestHeader("Content-Type", "application/json");



  xhr.responseType = 'json'

  xhr.onload = () => {
    const data = xhr.response
    document.getElementById('linkarea').value = data.newurl;

  }

  let data = {
    "url" : textvalue
  };

  xhr.send(JSON.stringify(data));

});