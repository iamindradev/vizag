var id= console.log(sessionStorage.getItem('id'));
function seedetails(){
    var xhttp =  new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:8000/studentdata/",true);
    xhttp.onreadystatechange = function()
    {
        console.log(this.readyState);
        xhttp.onload= function(){
            if(this.readyState==4 && this.status==200){
                console.log(this.responseText);
                document.getElementById("status").innerHTML= this.responseText
            }

        };
        
    }
    xhttp.send();


    

}

function raise(){
    
    rsquery ={lib:document.getElementById("lib").value,
            query:document.getElementById("query").value
}   
    console.log(rsquery )
    raisequery=JSON.stringify(rsquery);
    console.log(raisequery)
    var xhttp =  new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:8000/query/",true);
    xhttp.onreadystatechange = function()
    {
        console.log(this.readyState);
        xhttp.onload= function(){
            if(this.readyState==4 && this.status==200){
                console.log(this.responseText);
                document.getElementById("status").innerHTML= this.responseText
            }

        };
        
    }
    xhttp.send(raisequery);
}
function seestatus(){

}
function givedata(){
    document.getElementById("username").innerHTML=id;
}
