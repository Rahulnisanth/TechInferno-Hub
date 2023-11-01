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

//REMOVING TAGS USING API -->
let tags = document.getElementsByClassName("project-tag");
for (let i = 0; tags.length > i; i++) {
  tags[i].addEventListener("click", (e) => {
    let tagId = e.target.dataset.tag;
    let projectId = e.target.dataset.project;

    fetch("http://127.0.0.1:8000/api/remove-tag/", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ project: projectId, tag: tagId }),
    })
      .then((response) => response.json())
      .then((data) => {
        e.target.remove();
      });
  });
}
