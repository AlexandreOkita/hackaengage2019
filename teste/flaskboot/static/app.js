// Initialize Firebase(2)
var config = {
    apiKey: 'AIzaSyDbTLSOPNwsnCjm3rgYOqVGNt-uQLPK6EM',
    authDomain: 'malltup-hackengage.firebaseapp.com',
    databaseURL: 'https://malltup-hackengage.firebaseio.com"',
    storageBucket: 'projectId.appspot.com',
  };
  firebase.initializeApp(config);
  
  //Reference for form collection(3)
  let formMessage = firebase.database().ref('register');
  
  //listen for submit event//(1)
  document
    .getElementById('form')
    .addEventListener('submit', formSubmit);
  
  //Submit form(1.2)
  function formSubmit(e) {
    e.preventDefault();
    // Get Values from the DOM
    let titulo = document.querySelector('#titulo').value;
    let descricao = document.querySelector('#descricao').value;
    let local = document.querySelector('#local').value;
    let data = document.querySelector('#data').value;
  
    //send message values
    sendMessage(titulo, descricao, local, data);
  
  
    //Form Reset After Submission(7)
    document.getElementById('form').reset();
  }
  
  //Send Message to Firebase(4)
  
  function sendMessage(titulo, descricao, local, data) {
    let newFormMessage;
    newFormMessage.set({
      titulo: titulo,
      descricao: descricao,
      local: local,
      data: data,
    });
    formMessage.push(newFormMessage);
  }