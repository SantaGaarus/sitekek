window.scroll(0, localStorage.getItem("rerorerorero"));
if (!localStorage.getItem("a")==='[]' || !localStorage.getItem("a")){
    localStorage.setItem("a",JSON.stringify([]))
    
 }
if (!localStorage.getItem("ab")==='[]' || !localStorage.getItem("ab")){
    localStorage.setItem("ab",JSON.stringify([]))
    
 }
 if (!localStorage.getItem("abc")==='[]' || !localStorage.getItem("abc")){
    localStorage.setItem("abc",JSON.stringify([]))
    
 }
 if (!localStorage.getItem("abcd")==='[]' || !localStorage.getItem("abcd")){
   localStorage.setItem("abcd",JSON.stringify([]))
   
}
 function myFunction(name,image,price,url){
     const a = JSON.parse(localStorage.getItem('a'));
     const ab = JSON.parse(localStorage.getItem('ab'));
     const abc = JSON.parse(localStorage.getItem('abc'));
     const abcd = JSON.parse(localStorage.getItem('abcd'));
     a.push(name);
     ab.push(price);
     abc.push(image);
     abcd.push(url);
     localStorage.setItem("a",JSON.stringify(a));
     localStorage.setItem("ab",JSON.stringify(ab));
     localStorage.setItem("abc",JSON.stringify(abc));
     localStorage.setItem("abcd",JSON.stringify(abcd));
     localStorage.setItem("rerorerorero",window.scrollY)
}

if (!localStorage.getItem("al")==='[]' || !localStorage.getItem("al")){
   localStorage.setItem("al",JSON.stringify([]))
   
}
if (!localStorage.getItem("abl")==='[]' || !localStorage.getItem("abl")){
   localStorage.setItem("abl",JSON.stringify([]))
   
}
if (!localStorage.getItem("abcl")==='[]' || !localStorage.getItem("abcl")){
   localStorage.setItem("abcl",JSON.stringify([]))
   
}
if (!localStorage.getItem("abcdl")==='[]' || !localStorage.getItem("abcdl")){
  localStorage.setItem("abcdl",JSON.stringify([]))
  
}
function myLoveFunction(name,image,price,url){

    const al = JSON.parse(localStorage.getItem('al'));
    const abl = JSON.parse(localStorage.getItem('abl'));
    const abcl = JSON.parse(localStorage.getItem('abcl'));
    const abcdl = JSON.parse(localStorage.getItem('abcdl'));
    al.push(name);
    abl.push(price);
    abcl.push(image);
    abcdl.push(url);
    localStorage.setItem("al",JSON.stringify(al));
    localStorage.setItem("abl",JSON.stringify(abl));
    localStorage.setItem("abcl",JSON.stringify(abcl));
    localStorage.setItem("abcdl",JSON.stringify(abcdl));
   
}
