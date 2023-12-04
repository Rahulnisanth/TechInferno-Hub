document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("formInput#search");
  const searchResultsContainer = document.getElementById(
    "search-results-container"
  );

  searchInput.addEventListener("input", function () {
    const query = searchInput.value.trim();

    if (query.length === 0) {
      searchResultsContainer.innerHTML = "";
      return;
    }

    fetch(`/search/?q=${query}`)
      .then((response) => response.json())
      .then((data) => {
        searchResultsContainer.innerHTML = "";
        data.results.forEach((result) => {
          const resultItem = document.createElement("div");
          resultItem.classList.add("search-result-item");
          resultItem.innerHTML = `
                        <div class="column card">
                              <div class="dev">
                                    <a href="{% url 'single-profile' profile.id %}" class="card__body"
                                          style="padding-top: 1.7rem !important;">
                                          <div class="dev__profile">
                                                <img class="avatar avatar--md" src="{{profile.ImageURL}}" alt="image" />
                                                <div class="dev__meta">
                                                      <h3>{{profile.username}}</h3>
                                                      <h5>{{profile.job_role}}</h5>
                                                </div>
                                          </div>

                                          <p class="dev__info">
                                                {{profile.bio|slice:"150"}}
                                          </p>
                                          <div class="dev__skills">
                                                {% for skill in profile.skill_set.all|slice:":3" %}
                                                <span class="tag tag--pill tag--main">
                                                      <small>{{skill}}</small>
                                                </span>
                                                {% endfor %}
                                          </div>
                                    </a>
                              </div>
                        </div>
                    `;
          searchResultsContainer.appendChild(resultItem);
        });
      });
  });
});
