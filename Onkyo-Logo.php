<html>
<head>
<title>Onkyo-Logo</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<!-- Save for Web Slices (Onkyo-Logo.jpg) -->
<table id="Tabelle_01" width="237" height="195" border="0" cellpadding="0" cellspacing="0">
	<tr>
		<td colspan="5">
			<img src="Bilder/Onkyo-Logo_01.jpg" width="237" height="124" alt=""></td>
	</tr>
	<tr>
		<td>
<img src="Bilder/Onkyo-Logo_02.jpg" width="21" height="71" alt=""></td>
		<td>

			<a href="?OFF" method="POST"> <img src="Bilder/Onkyo-Off.jpg" width="76" height="71" alt="Onkyo-Off"></a></td>
		<td>
			<img src="Bilder/Onkyo-Logo_04.jpg" width="47" height="71" alt=""></td>
		<td>
<a href="?ON" method="POST">			<img src="Bilder/Onkyo-On.jpg" width="76" height="71" alt="Onkyo-On"></td>
		<td>
			<img src="Bilder/Onkyo-Logo_06.jpg" width="17" height="71" alt=""></td>
	</tr>
</table>
<!-- End Save for Web Slices -->
 <?php IF (isset( $_REQUEST['OFF'])) 
 {
$output=shell_exec('/usr/local/bin/onkyo PWR00');
echo "<pre>.$output</pre>";
 }         					
 
 elseif (isset( $_REQUEST['ON'])) 		
 {
 	$output=shell_exec('/usr/local/bin/onkyo PWR01');
echo "<pre>.$output</pre>";

 }
 else {}

?>
</body>
</html>

