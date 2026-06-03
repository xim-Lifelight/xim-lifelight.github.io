/*
var CONFIG = {
  dateOfIssue:     "27/05/26",
  revision:        "10",
  mfgDate:         "(11)260527",
  softwareVersion: "(8012)6.0.1-0",
  labelMfgDate:    "05 2026",
  changeControl: {
    "en":     "refer to e-QMS",
    "de":     "siehe e-QMS",
    "es":     "consultar el e-QMS",
    "es-LAT": "consultar el e-QMS",
    "fr":     "se référer à l'e-QMS",
    "it":     "fare riferimento all'e-QMS",
    "nl":     "zie e-QMS",
    "th":     "โปรดดู e-QMS"
  }
};

document.addEventListener('DOMContentLoaded', function() {
  var c = CONFIG;
  var set = function(cls, val) {
    document.querySelectorAll('.' + cls).forEach(function(el) { el.textContent = val; });
  };
  set('ifu-date', c.dateOfIssue);
  set('ifu-revision', c.revision);
  set('ifu-mfgDate', c.mfgDate);
  set('ifu-software-version', c.softwareVersion);
  set('label-mfg-date', c.labelMfgDate);
  var lang = document.documentElement.dataset.lang || 'en';
  set('ifu-change-control', c.changeControl[lang] || c.changeControl['en']);
});
*/
