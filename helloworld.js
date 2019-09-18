function hello () {
	//向世界问好
	var mydate = new Date();
	alert(mydate);
}

// function Person(name, age)
// {
// this.name = name;
// this.age = age;
// this.show = function(){
// var res = "我是 " + this.name + "  年龄 " + this.age +".";
// return res;
// };
// }


// // 给person添加几个属性
// Person.prototype.gender = "女";
// Person.prototype.getSex = function(){
// return this.gender;
// };
 
// //定义学生对象
// function Student(num){
// this.num=num;
// }
 
// Student.prototype=new Person("alice",23);
// var s=new Student(123434);
// console.log(s.show());



// $(document).ready(function(){
// 	animate();
//   $(".play").click(animate).mouseover(function(){
//   	$(".play").css({"background-color":"#A55"});
//   }).mouseout(function(){
//   	$(".play").css({"background-color":"#060"});
//   });
// });
// function animate(){
// 	  $('div>div>div').each(function(id){
//     $(this).css({
//       position: 'relative',
//       top: '-200px',
//       opacity: 0
//     });
//     var wait = Math.floor((Math.random()*3000)+1);
//     $(this).delay(wait).animate({
//       top: '0px',
//       opacity: 1
//     },1000);
//   });
// }

