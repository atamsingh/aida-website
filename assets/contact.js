// Sends the on-page contact form to the Google Form behind it, then shows a
// thank-you message without leaving the page.
(function () {
  var form = document.querySelector('.contact-form');
  if (!form) return;
  var done = form.parentNode.querySelector('.form-done');
  var error = form.querySelector('.form-error');
  var button = form.querySelector('button[type="submit"]');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    error.hidden = true;
    var f = form.elements;
    if (f.website.value) { finish(); return; } // spam trap

    var comments = [
      'Topic: ' + f.topic.value,
      f.company.value ? 'Organization: ' + f.company.value : '',
      'Sent from: ' + form.dataset.page + ' page',
      '',
      f.message.value
    ].filter(function (line, i) { return line !== '' || i === 3; }).join('\n');

    var body = new URLSearchParams();
    body.append(form.dataset.name, f.name.value);
    body.append(form.dataset.email, f.email.value);
    if (f.phone.value) body.append(form.dataset.phone, f.phone.value);
    body.append(form.dataset.comments, comments);

    button.disabled = true;
    button.textContent = 'Sending…';
    // Google Forms does not allow the reply to be read, so "no-cors" is
    // required; a network failure still rejects and shows the error.
    fetch(form.action, { method: 'POST', mode: 'no-cors', body: body })
      .then(finish)
      .catch(function () {
        error.hidden = false;
        button.disabled = false;
        button.textContent = 'Send message';
      });
  });

  function finish() {
    form.hidden = true;
    done.hidden = false;
    done.focus();
    // Hook for ad conversion tracking once Google tag is installed.
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: 'contact_form_submit', page: form.dataset.page });
  }
})();
