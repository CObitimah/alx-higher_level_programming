$(document).ready(function () {
	function fetchTranslate() {
		const languageCode = $('#language_code').val();
		const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
		$.get(url, function(data) {
			$('#hello').text(data.hello);
		});
	}

	$('#btn_translate').click(fetchTranslation);

	$('#language_code').keypress(function(event) {
		if (event.which === 13) { // Enter key pressed
			fetchTranslation();
		}
	});
});
