function takeinput(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    myobj={username: username, password: password} ;
    data= JSON.stringify(myobj);
    console.log(data)

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:8000/login/",true);
    xhttp.onreadystatechange = function()
    {

        console.log(xhttp.readyState)
        
        
        xhttp.onload = function(){
            if(this.readyState==4 && this.status === 200){
            console.log(this.responseText)
            // document.getElementById("return").innerHTML = this.responseText;
            data = JSON.parse(this.responseText)
            console.log(data)
            value = data['value']
            console.log(value)
            if (value == "welcome student"){
                window.open("studentds.html")
                
            }
            else if(value =="welcome teacher"){
                window.open("teacherds.html")
                
            }
        }
        else{
            console.log ("some error occured")
        }
    }
    };
    
    xhttp.send(data)
    console.log(myobj)
    var store=sessionStorage.setItem("lib",data);
    console.log(store)

}
function givedata()
    {
        
        student_data=data['b']
        this.addEventListener("load",givedata);
        alert('welcome'+student_data+'hey');
        
    }  
function openhome(){
    window.open("homepage.html");
}