// Sends the contact form to Web3Forms, which emails the enquiry and reports
// whether it was accepted. A copy also goes to the Google Form as a silent
// backup. The thank-you message is shown only after Web3Forms confirms.
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
    if (f.botcheck.checked) { showThanks(); return; } // spam trap: pretend it worked

    var page = form.dataset.page;
    var payload = {
      access_key: f.access_key.value,
      from_name: f.from_name.value,
      subject: 'New enquiry: ' + f.topic.value,
      name: f.name.value,
      email: f.email.value,
      organization: f.company.value,
      phone: f.phone.value,
      topic: f.topic.value,
      message: f.message.value,
      page: page + ' page'
    };

    button.disabled = true;
    button.textContent = 'Sending…';

    fetch(form.action, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(function (res) { return res.json().catch(function () { return { success: false }; }); })
      .then(function (data) {
        if (!data || !data.success) throw new Error('not accepted');
        backup(payload);
        showThanks();
        // Hook for ad conversion tracking once a Google tag is installed.
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ event: 'contact_form_submit', page: page });
      })
      .catch(function () {
        backup(payload); // still try to keep a copy of the enquiry
        error.hidden = false;
        button.disabled = false;
        button.textContent = 'Send message';
      });
  });

  // Best-effort copy to the Google Form. Its reply cannot be read, and a
  // failure here never affects what the visitor sees.
  function backup(p) {
    if (!form.dataset.backup) return;
    var comments = [
      'Topic: ' + p.topic,
      p.organization ? 'Organization: ' + p.organization : null,
      'Sent from: ' + p.page,
      '',
      p.message
    ].filter(function (line) { return line !== null; }).join('\n');
    var body = new URLSearchParams();
    body.append(form.dataset.name, p.name);
    body.append(form.dataset.email, p.email);
    if (p.phone) body.append(form.dataset.phone, p.phone);
    body.append(form.dataset.comments, comments);
    try {
      fetch(form.dataset.backup, { method: 'POST', mode: 'no-cors', body: body }).catch(function () {});
    } catch (err) { /* ignore */ }
  }

  function showThanks() {
    form.hidden = true;
    done.hidden = false;
    done.focus();
  }
})();
