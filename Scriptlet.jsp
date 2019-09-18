<%@ page contentType="text/html;charset=gb2312"%>

<html>
<head>
	<title>
		

	</title>
</head>
<body charset="utf-8">
<p>Hi</p>

<!--这个注释会发送到客户端<%=new java.util.Date()%>-->
<%--这个注释不会发送到客户端--%>

<%
	for(int i = 0; i< 10; ++i){
	    out.printin("编号:"+i);
		out.printin("<br>");
	}
%>

<hr>

<%
	string a,b;
	a = "Hello";
	b = "Scriptlet";
	out.printin(a + " " + b);
%>

</body>

</html>


