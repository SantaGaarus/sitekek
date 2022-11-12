const al=JSON.parse(localStorage.getItem('al'));
const abl=JSON.parse(localStorage.getItem('abl'));
const abcl=JSON.parse(localStorage.getItem('abcl'));
const abcdl=JSON.parse(localStorage.getItem('abcdl'));
var sum=0;
function generateList(arg,arg1,arg2,arg3){
    let items="";
    for (let i=0; i<arg.length;i++){
        console.log(arg1[i])
        items+=`<li class='mebel_blockk'>
        <a>${arg[i]}</a> </br> </br>

         <a href=${arg3[i]}> <img  class="mebel_img"  src=${window.location.href.replace('nravit','media/'+arg2[i])}></a>
         </br>
         <a>${arg1[i]} ₽ </a>
         <a href='' onclick= "del('${arg[i]}')" class='korz'>удалить</a>
        </br>
        </br>
        
        </li>`;
       
    }
    return items;
    
}

function del(name){
    
    const al = JSON.parse(localStorage.getItem('al'));
    const abl = JSON.parse(localStorage.getItem('abl'));
    const abcl = JSON.parse(localStorage.getItem('abcl'));
    const abcdl = JSON.parse(localStorage.getItem('abcdl'));
    abl.splice(al.indexOf(name), 1); 
    abcl.splice(al.indexOf(name), 1); 
    abcdl.splice(al.indexOf(name), 1);
    al.splice(al.indexOf(name), 1);  
    localStorage.setItem("al",JSON.stringify(al));
    localStorage.setItem("abl",JSON.stringify(abl));
    localStorage.setItem("abcl",JSON.stringify(abcl));
    localStorage.setItem("abcdl",JSON.stringify(abcdl));

}

document.querySelector(".zs").innerHTML=`
<ul>
${generateList(al,abl,abcl,abcdl)}
</ul>
`;


