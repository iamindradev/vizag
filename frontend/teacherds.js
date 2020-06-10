function seedetails(){
    var value="";
    var xhttp= new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:8000/login/teacher/", true);
    xhttp.onreadystatechange=function(){
        console.log(this.readyState)
        xhttp.onload=function(){
            if (this.readyState==4 && this.status==200){
            console.log(this.responseText)
            data=JSON.parse(this.responseText);
            console.log(data)
            for (x in data){
                value+="<tr><td>"+ data[x].lib_id+"</td><td>"+ data[x].name + "</td><td>"+ data[x].father_name+
                "</td><td>"+ data[x].email + "</td><td>"+ data[x].branch+"</td><td>"
                + data[x].section + "</td><td>"+ data[x].contact+"</td><td>"
                + data[x].Dob + "</td><td>"+ data[x].address+
                "</td><td><button id ="+x+" onclick="+"input()"+">update</button></td><td><button>delete</button></td></tr>"
                    
            document.getElementById("table").innerHTML= value;
            } 
        }
    }
}
    xhttp.send();
    
}
function input(){
    
    window.open("update.html")
}

function update(){
    obj={ lib_id:document.getElementById("lib_id").value}
    myobj=JSON.stringify(obj);
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:8000/login/teacher/update",true);
    xhttp.onreadystatechange=function(){
        console.log(this.readyState)
        xhttp.onload=function(){
            if(this.readyState==4 && this.status==200){
                console.log(this.responseText)
                document.getElementById("confirmdata").innerHTML=this.responseText
        }
    };
    xhttp.send(myobj);
}
}

function addstudent(){
    myobj={
        lib:document.getElementById("lib").value,
        name: document.getElementById("name").value,
        father_name: document.getElementById("fname").value,
        email: document.getElementById("email").value,
        branch: document.getElementById("branch").value,
        section: document.getElementById("section").value,
        contact: document.getElementById("cno").value,
        Dob: document.getElementById("dob").value,
        address: document.getElementById("address").value,

}
addstd=JSON.stringify(myobj);

console.log(myobj)
console.log(addstd)
var xhttp = new XMLHttpRequest();
xhttp.open("POST","http://127.0.0.1:8000/login/teacher/addstudent", true);
xhttp.onreadystatechange=function()
{
    console.log(this.readyState)
    xhttp.onload=function(){
        if(this.readyState==4 && this.status==200){
            console.log(this.responseText)
            document.getElementById("confirmdata").innerHTML=this.responseText

        }
    }
}
xhttp.send(addstd)
}



function giveapprove(){
    var value="";
    var xhttp = new XMLHttpRequest();
xhttp.open("POST","http://127.0.0.1:8000/seequery/", true);
xhttp.onreadystatechange=function()
  {
        console.log(this.readyState)
        xhttp.onload=function(){
            if(this.readyState==4 && this.status==200){
                console.log(this.responseText)
                
                
                data=JSON.parse(this.responseText);
                console.log(data)
                for (x in data){
                value+="<tr><td>"+ data[x].lib+"</td><td>"+ data[x].query +
                "</td><td><button>APPROVE</button></td><td><button>REJECT</button></td></tr>"
                    
                document.getElementById("table").innerHTML= value;
    
            }
        }
    };
    
    }
    xhttp.send();
}