function deleteNote(noteId){
  fetch('/deleteNote',{
    method : 'POST',
    body : JSON.stringify({noteId : noteId}),
  }).then((res)=>{
    window.location.href = '/'
  })
}