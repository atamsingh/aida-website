// Filters the blog list by topic and by search text. Posts are already in
// newest-first order in the page.
(function () {
  var cards = [].slice.call(document.querySelectorAll('.blog-list .post-card'));
  var chips = [].slice.call(document.querySelectorAll('.blog-filters .chip'));
  var input = document.querySelector('.blog-search input');
  var empty = document.querySelector('.blog-empty');
  var tag = '';

  function apply() {
    var words = input.value.toLowerCase().split(/\s+/).filter(Boolean);
    var shown = 0;
    cards.forEach(function (card) {
      var ok = (!tag || card.dataset.tag === tag) &&
        words.every(function (w) { return card.dataset.text.indexOf(w) !== -1; });
      card.hidden = !ok;
      if (ok) shown++;
    });
    empty.hidden = shown !== 0;
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      tag = chip.dataset.filter;
      chips.forEach(function (c) { c.classList.toggle('is-active', c === chip); });
      apply();
    });
  });
  input.addEventListener('input', apply);
})();
