const aaa=JSON.parse(localStorage.getItem('a'));
const ab=JSON.parse(localStorage.getItem('ab'));
const abc=JSON.parse(localStorage.getItem('abc'));
const abcd=JSON.parse(localStorage.getItem('abcd'));
var sum=0;
var names="";
var blog="{% url 'blog:detail_barstul' i.id %}"

function generateList(arg,arg1,arg2,arg3){
    let items="";
    for (let i=0; i<arg.length;i++){
        console.log(arg1[i])
        items+=`<li class='mebel_blockk'>
        <a>${arg[i]}</a> </br> </br>

         <a href=${arg3[i]}> <img  class="mebel_img"  src=${window.location.href.replace('korzina','media/'+arg2[i])}></a>
         </br>
         <a>${arg1[i]} ₽ </a>
         <a href='' onclick= "del('${arg[i]}')" class='korz'>удалить</a>
        </br>
        </br>
        
        </li>`;
        sum+=Number(arg1[i]);
        names+=String(i+"."+arg[i]);
        document.querySelector(".summakoplat").innerHTML=`${sum} ₽`
        document.querySelector(".summakoplat1").innerHTML=`${sum} ₽`
        document.getElementById("zakazi").value+=arg[i]
    }
    document.getElementById("obj_tsen").value =parseFloat(sum)
    document.getElementById("obj_tsen1").value =parseFloat(sum)
    document.getElementById("zakazi").value=localStorage.getItem('a')
    document.getElementById("zakazi1").value=localStorage.getItem('a')
    return items;
    
}
function degro(){
    if(document.querySelector('.filter_btnControl').checked===false){
        document.querySelector('.oplata_blanc').style='margin-left: 20%;';
    }
    if(document.querySelector('.filter_btnControl').checked===true){
        document.querySelector('.oplata_blanc').style='margin-left: 100%;';
    }
    }
function del(name){
    
    const a = JSON.parse(localStorage.getItem('a'));
    const ab = JSON.parse(localStorage.getItem('ab'));
    const abc = JSON.parse(localStorage.getItem('abc'));
    const abcd = JSON.parse(localStorage.getItem('abcd'));
    ab.splice(a.indexOf(name), 1); 
    abc.splice(a.indexOf(name), 1); 
    abcd.splice(a.indexOf(name), 1);
    a.splice(a.indexOf(name), 1);  
    localStorage.setItem("a",JSON.stringify(a));
    localStorage.setItem("ab",JSON.stringify(ab));
    localStorage.setItem("abc",JSON.stringify(abc));
    localStorage.setItem("abcd",JSON.stringify(abcd));

}



function Freak(){
    localStorage.clear()

  }  
document.querySelector(".zs").innerHTML=`
<ul>
${generateList(aaa,ab,abc,abcd)}
</ul>
`;


