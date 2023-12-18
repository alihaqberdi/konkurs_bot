import requests


def translate(text, lang="en", to_lang='uz'):
	url = "https://text-translator2.p.rapidapi.com/translate"

	payload = {
		"source_language": lang,
		"target_language": to_lang,
		"text": text
	}
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": "a304e57309msh900825cb64644c9p1b123cjsn3317dfb517b1",
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}

	response = requests.post(url, data=payload, headers=headers)
	return response.json().get('data').get("translatedText")

