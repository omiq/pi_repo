<script>
window.setInterval(function(){
	var newImage = new Image();
	newImage.src = "/webcam.jpg?"+new Date().getTime();
	jQuery("#webcam").attr("src",newImage.src);

},200);
</script>
