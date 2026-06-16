window.openCalendly = function(el) {
  var label = el.innerHTML;

  el.innerHTML = '⏳ Chargement du calendrier...';
  el.setAttribute('aria-busy', 'true');
  el.style.opacity = '0.72';
  el.style.pointerEvents = 'none';

  var restore = function() {
    el.innerHTML = label;
    el.removeAttribute('aria-busy');
    el.style.opacity = '';
    el.style.pointerEvents = '';
  };

  // Safety net: restore after 8s if something goes wrong
  var safetyTimer = setTimeout(restore, 8000);

  try {
    if (typeof Calendly === 'undefined') throw new Error('Calendly not loaded');
    Calendly.initPopupWidget({ url: 'https://calendly.com/techerchristopher/30min' });
    // Popup is open — restore button after 2s so user can re-click if needed
    clearTimeout(safetyTimer);
    setTimeout(restore, 2000);
  } catch(e) {
    clearTimeout(safetyTimer);
    restore();
  }
};
