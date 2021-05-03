/**
 Credit to openweathermap.org to provide us with an api so that we can use the functionalities to show the weather of surrounding 
 */
function getI18n(key, lang) {
	var i18n = {
		en: {
			  maps: 'Maps'
			, layers: 'TileLayer'
			, current: 'Current Weather'

			, clouds: 'Clouds'
			, cloudscls: 'Clouds with a legend'
			, precipitation: 'Precipitation'
			, precipitationcls: 'Precipitation with a legend'
			, rain: 'Rain'
			, raincls: 'Rain with a legend'
			, snow: 'Snow'
			, temp: 'Temperature'
			, windspeed: 'Wind Speed'
			, pressure: 'Pressure'
			, presscont: 'Pressure Contour'

			, city: 'Cities'
			, windrose: 'Wind Rose'

			//, prefs: 'Preferences'
			//, scrollwheel: 'Scrollwheel'
			//, on: 'on'
			//, off: 'off'
		}		
	};

	if (typeof i18n[lang] != 'undefined'
			&& typeof i18n[lang][key] != 'undefined') {
		return  i18n[lang][key];
	}
	return key;
}


function getLocalLanguage() {
	var lang = null;

	
	var qs = window.location.search;
	if (qs) {
		if (qs.substring(0, 1) == '?') {
			qs = qs.substring(1)
		}
		var params = qs.split('&')
		for(var i = 0; i < params.length; i++) {
			var keyvalue = params[i].split('=');
			if (keyvalue[0] == 'lang') {
				lang = keyvalue[1];
				break;
			}
		}
	}

	
	if (!lang) {
		var tmp = window.navigator.userLanguage || window.navigator.language;
		lang = tmp.split('-')[0];
	}

	
	if (lang != 'en') {
		lang = 'en';
	}
	return lang;
}

