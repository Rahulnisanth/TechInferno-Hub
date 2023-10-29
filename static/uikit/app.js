// Invoke Functions Call on Document Loaded
document.addEventListener("DOMContentLoaded", function () {
  hljs.highlightAll();
});

//ALERT LOG ->
let alertWrapper = document.querySelector(".alert");
let alertClose = document.querySelector(".alert__close");

if (alertWrapper) {
  alertClose.addEventListener("click", () => {
    alertWrapper.style.display = "None";
  });
}
