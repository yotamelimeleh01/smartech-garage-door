(function () {
  var HOOK = "https://hook.us2.make.com/98l8grun2b3ubw0xolbb5m8kb5iywggc";

  var btn = document.querySelector(".menu-btn"), nav = document.querySelector(".nav");
  if (btn && nav) btn.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });

  document.querySelectorAll("form.quote").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var phone = (f.phone.value || "").replace(/\D/g, "");
      if (phone.length < 10) { alert("Please enter a valid 10-digit phone number."); f.phone.focus(); return; }
      var b = f.querySelector("button[type=submit]");
      b.disabled = true; b.textContent = "Sending...";
      var data = new URLSearchParams(new FormData(f));
      data.append("page", location.pathname);
      fetch(HOOK, { method: "POST", body: data, mode: "no-cors" })
        .then(function () {
          if (window.fbq) window.fbq("track", "Lead");
          location.href = f.getAttribute("data-thanks");
        })
        .catch(function () {
          b.disabled = false; b.textContent = "Try again";
          alert("Something went wrong. Please call us instead.");
        });
    });
  });
})();
