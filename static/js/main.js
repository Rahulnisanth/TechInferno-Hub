//PAGINATION SEARCH SNIPPET ->

let searchForm = document.querySelector("#searchForm");
let pageLinks = document.getElementsByClassName(".page-lnk");
for (let i = 0; i < pageLinks.length; i++) {
  pageLinks[i].addEventListener("click", function (e) {
    e.preventDefault();
    let page = this.dataset.page;
    searchForm.innerHTML += `<input value=${page} name="page" hidden />`;
    searchForm.submit();
  });
}
