function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }
  
  //Calculator aport proteic in functie de training lvl
function ProteinCalculator(){
    let kg;
    let lvl;
    kg = parseInt(document.getElementById("i1").value);
    lvl = document.getElementById("optiuni").value;
    let result;
    if(lvl == "Sedentary")
    {
      result = kg*0.8;
    }
    if(lvl == "Moderate Activity") 
    {
      result = kg;
    }
    if(lvl == "Endurance Training") 
    {
      result= kg*1.2;
    }
    if(lvl == "Weight Training")
    {
      result= kg*1.6;
    }
    document.getElementById("rez").innerHTML = result;
  
}
  
  function ProteinCalculator(){
    let kg;
    let lvl;
    kg = parseInt(document.getElementById("i1").value);
    lvl = document.getElementById("optiuni").value;
    let result;
    if(lvl == "Sedentary")
    {
        result = kg*0.8;
    }
    if(lvl == "Moderate Activity") 
    {
        result = kg;
    }
    if(lvl == "Endurance Training") 
    {
        result= kg*1.2;
    }
    if(lvl == "Weight Training")
    {
        result= kg*1.6;
    }
    document.getElementById("rez").innerHTML = result;

}