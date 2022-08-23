var list = [
  "a001","a002","a003","a004","a005","a006","a007","a008","a009","a010","a011"
];
var ach_name = [
  "冰冰姐殺手",
  "YAGOO我婆",
  "わためは悪くないよねぇ",
  "どうも、湊あくあです",
  "はあちゃまちゃま",
  "はあと...？",
  "我愛墨西哥粽",
  "我愛冰冰姐",
  "我全都要",
  "墨西哥粽狂熱粉",
  "墨西哥粽小達人"
];
var ach_how = [
  "接到200個冰冰姐",
  "接到100個YAGOO",
  "接到100個わため",
  "接到100個あくあ",
  "進入三次はあちゃま cooking",
  "進入五次Doki Doki haachama club",
  "獲得500分且沒有接到任何冰冰姐",
  "獲得500分且沒有接到任何墨西哥粽",
  "獲得500分且接到冰冰姐與墨西哥粽數量相同",
  "獲得1500分且沒有接到任何冰冰姐",
  "接到200個墨西哥粽"
];
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
var my_name = getCookie("Username"),ach_str="";
if(my_name==""){
  window.location.href = "https://hotpot.guaichi.repl.co/";
}
else{
  document.getElementById("User_title").innerHTML = "使用者「"+my_name+"」";
  for(var i=0;i<11;i++){
    if(getCookie(list[i])!="0"){
      ach_str += ach_name[i] + "：" + ach_how[i] + "<br>"
    }
  }
  document.getElementById("i_have").innerHTML = ach_str;
}