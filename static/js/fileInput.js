// document.addEventListener("DOMContentLoaded", function () {
//   document
//     .querySelector('input[type="file"]')
//     .addEventListener("change", function (e) {
//       const preview = document.getElementById("image-preview");
//       const file = e.target.files[0];

//       if (file) {
//         const reader = new FileReader();
//         reader.onload = function (readerEvent) {
//           preview.src = readerEvent.target.result;
//         };
//         reader.readAsDataURL(file);
//       } else {
//         preview.src =
//           "{% if form.instance.profile_picture %}{{ form.instance.profile_picture.url }}{% endif %}";
//       }
//       console.log(preview.src);
//     });
// });

document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.querySelector('input[type="file"]');

  if (fileInput) {
    fileInput.addEventListener("change", function (e) {
      const preview = document.getElementById("image-preview");
      const file = e.target.files[0];

      if (file) {
        const reader = new FileReader();
        reader.onload = function (readerEvent) {
          preview.src = readerEvent.target.result;
        };
        reader.readAsDataURL(file);
      } else {
        preview.src =
          "{% if form.instance.profile_picture %}{{ form.instance.profile_picture.url }}{% endif %}";
      }
      console.log(preview.src);
    });
  } else {
    console.error("File input element not found.");
  }
});
