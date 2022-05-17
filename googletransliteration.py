type="text/javascript"
  google.load("elements", "1", {
  packages: "transliterate"
  })
  function onLoad() {
        var options = {
          sourceLanguage: 'it',
          destinationLanguage: ['ru'],
          transliterationEnabled: true
        };
    var control =
            new google.elements.transliteration.TransliterationControl(options);
    var ids = [ "altalena", "nascondino" ];
        control.makeTransliteratable(ids);
