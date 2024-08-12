
//username generation---->
function validatedata(){
    var yr = document.getElementById('clgname');

    var first5 = yr.value.substring(0,5);

    var rollno=document.getElementById('rollno');

    var username=document.getElementById('username');
    username.value=clgcode.value+first5;
    console.log(username.value);


    return username;
    }
    document.getElementById('username').addEventListener("mouseover",validatedata);



