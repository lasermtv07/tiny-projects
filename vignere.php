<?php
// (c)lasermtv07, 2024
// this program is free software distributed under terms of WTFPL 2.0
// this program is distributed in good faith; however without any warranty, including any implied warranty
?>

<!DOCTYPE HTML>
<html>
<head>
	<title>vignere cipher</title>
	<style>
		.out {
			color:white;
			background-color:blue;
			padding: 10px;
		}
	</style>
</head>
<body>
<h1>Vignere cipher</h1>
<p>A fun challenge I have been meaning to try. The Vignere cipher has been invented in the 1500s in France, however was unbeaten until the
<a href="https://en.wikipedia.org/wiki/Kasiski_examination">Kasiski attack</a> has been discovered in <b>the second half of 19th century</b>.
I would describe it here but I hadnt yet gone that far. Vignere cipher is a <b>polyalphabetic substitution cipher</b> meaning that it has
more than one alphabets. Substitution meaning that instead of the plaintext being shuffled, it is replaced.
</p>
<p>
The alphabets that nerds mark with &Sigma; are based on something called <i><b>tabuli recta</b></i>. Essentially, every alphabet is shifted so
that the <b>key</b> letter is the first in the alphabet and others wrap around it. So alphabet of key <b>B</b> start with B, then C, D.. etc.
Alphabet of <b>Z</b> starts at.. Z, then wraps around to A,B,C.. Then you just take the letter from plaintext, find its position on the keys alphabet,
write it down and continue. The advantage is that the key can be <b>longer than one character</b>, so its much safer than the <a href="https://en.wikipedia.org/wiki/Caesar_cipher">Caesar cipher</a>.. y'know, if u dont get my <strike>terrible</strike> perfect explanation, go read the Wikipedia article.
</p>
<p>
<b>Sources:</b> <i>[<a href="https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher">wikipedia</a>] [<a href="https://www.britannica.com/topic/cryptology/Vigenere-ciphers">brinnanica</a>]</i>
<hr/>
<?php
$msg=isset($_GET["input"]) ? $_GET["input"] : "attackatdown";
$key=isset($_GET["key"]) ? $_GET["key"] : "lemon";
$cipher=isset($_GET["input"]) ? $_GET["input"] : "attackatdown";
?>

<form method="get">
<b>Input: </b> <input type="text" placeholder="Input" name="input" value="<?php echo "$msg"; ?>"/><br>
<b>Key:&nbsp;&nbsp;&nbsp;&nbsp; </b> <input type="text" placeholder="Key" name="key" value="<?php echo "$key"; ?>" /><br>
<b>Operation: </b> <input type="radio" name="op" value="enc"> Encrypt | <input type="radio" name="op" value="dec"> Decrypt<br>
<input type="submit" />
</form>
<br>
<h3>Output:</h3>
<div class=out>
<?php

$op=(!isset($_GET["op"]) || $_GET["op"]=="enc");
$alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
$tr=[];

//extend key to lenght $l
function extend($k,$l){
	while(strlen($k)<=$l){
		$k.=$k;
	}
	$k=str_split($k);
	while(sizeof($k)>$l){
		array_pop($k);
	}
	$k=implode("",$k);
	return $k;
}
//shifts input alphabet so $l element is the first
function shiftAlphabet($a,$l){
	$s=array_search($l,$a);
	$na=$a;
	foreach($na as $k=>$i){
		$si=$k+$s;
		if($si<sizeof($a)) $na[$k]=$a[$si];
		else  $na[$k]=$a[$si-sizeof($a)];
	}
	return $na;
}
//if youre wondering why the variable names and shit got better dont worry about it
//ive had coffee
function encrypt($msg,$key,$tr,$alph){
	$key=str_split($key);
	$encrypted="";
	$skip=0;
	foreach(str_split($msg) as $k=>$i){
		if(array_key_exists($i,$tr)){
			$encrypted.=$tr[$key[$k-$skip]][array_search($i,$alph)];
		}
		else {
			$skip++;
			$encrypted.=$i;
		}
	}
	return $encrypted;
}


//generate extended key
$key=extend($key,strlen($msg));
$key=strtolower($key);
$msg=strtolower($msg);
$cipher=strtolower($cipher);
//generate tabula recta
foreach($alph as $i){
	$tr[$i]=shiftAlphabet($alph,$i);
}


function decrypt($cipher,$key,$tr,$alph){
	$key=str_split($key);
	$skip=0;
	$dmsg=""; //my codes becoming dirty mess atp, so i use there weird names to avoid collision
	foreach(str_split($cipher) as $k=>$i){
		if(array_key_exists($i,$tr)){
			$dmsg.=$alph[array_search($i,$tr[$key[$k-$skip]])];
		}
		else {
			$skip++;
			$dmsg.=$i;
		}
	}
	return $dmsg;
}

if($op)echo encrypt($msg,$key,$tr,$alph);
else echo decrypt($cipher,$key,$tr,$alph);
?>
</div>
</body>
</html>
