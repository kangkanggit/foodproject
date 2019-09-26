
var code;

//产生验证码
window.onload = function  () {
	
	function_name();
	
}

//生成验证码
function function_name () {
	
	code = "";
	var codeLength = 4;//验证码长度
	var checkCode = document.getElementById("code");
	var random = new Array(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
	 'S','T','U','V','W','X','Y','Z');//随机数
	 
	 for (var i = 0; i < codeLength; i++) {
	 		
	 		//随机生成下标
	 		var index = Math.floor(Math.random()*36); //获取随机数的索引（0-35）
	 		code+=random[index];
	 		
	 }
	 
	 //把code值赋值给验证码
	 checkCode.value= code;
	
}

//校验验证码
function validate(){
	
	//获取输入框的数值
	var inputCode = document.getElementById("input").value.toUpperCase();
	
	if (inputCode.length<=0) {
		alert("请输入验证码！")
		
	}else if (inputCode !=code) {
		
		alert("验证码输入有误！")//提示输入有误
		function_name(); //调用函数，重新生成验证码
		document.getElementById("input").value="";//清空文件框
		
		
	}else{
		
		alert("输入正确");
		
	}
	
}

































