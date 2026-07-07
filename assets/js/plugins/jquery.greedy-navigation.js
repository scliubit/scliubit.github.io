/*
* Greedy Navigation
*
* http://codepen.io/lukejacksonn/pen/PwmwWV
*
*/

var $nav = $('#site-nav');
var $btn = $('#site-nav .greedy-nav__toggle');
var $vlinks = $('#site-nav .visible-links');
var $hlinks = $('#site-nav .hidden-links');
var $controls = $('#site-nav .nav-controls');

var breaks = [];

function updateNav() {

  var controlsRight = parseFloat($controls.css('right')) || 0;
  var controlsSpace = $controls.length ? $controls.outerWidth(true) + controlsRight : 0;
  var availableSpace = $nav.width() - controlsSpace - 30;
  var $lastMovable = $vlinks.children('*:not(.masthead__menu-item--lg):not(.persist)').last();

  // The visible list is overflowing the nav
  if($vlinks.width() > availableSpace && $lastMovable.length) {

    // Record the width of the list
    breaks.push($vlinks.width());

    // Move item to the hidden list
    $lastMovable.prependTo($hlinks);

    // Show the dropdown btn
    if($btn.hasClass('hidden')) {
      $btn.removeClass('hidden');
    }

  // The visible list is not overflowing
  } else {

    // There is space for another item in the nav
    if(availableSpace > breaks[breaks.length-1]) {

      // Move the item to the visible list
      $hlinks.children().first().appendTo($vlinks);
      breaks.pop();
    }

    // Hide the dropdown btn if hidden list is empty
    if(breaks.length < 1) {
      $btn.addClass('hidden');
      $hlinks.addClass('hidden');
    }
  }

  // Keep counter updated
  $btn.attr("count", breaks.length);

  // Recur if the visible list is still overflowing the nav
  if($vlinks.width() > availableSpace && $vlinks.children('*:not(.masthead__menu-item--lg):not(.persist)').length) {
    updateNav();
  }

}

// Window listeners

$(window).resize(function() {
  updateNav();
});

$btn.on('click', function() {
  $hlinks.toggleClass('hidden');
  $(this).toggleClass('close');
});

updateNav();
