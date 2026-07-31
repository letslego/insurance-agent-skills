(function () {
  const skills = window.UNDERWRITER_SKILLS || [];
  const list = document.getElementById("skill-list");

  if (list) {
    list.innerHTML = skills
      .map(
        (skill, index) => `
      <article class="skill" data-skill="${skill.id}" style="animation-delay: ${index * 30}ms">
        <button class="skill-toggle" type="button" aria-expanded="false">
          <span>
            <span class="skill-name">${skill.name}</span>
            <span class="skill-command">${skill.command}</span>
          </span>
          <span class="skill-blurb">${skill.blurb}</span>
          <span class="skill-chevron" aria-hidden="true">+</span>
        </button>
        <div class="skill-body">
          <div>
            <h3>When to use</h3>
            <p>${skill.when}</p>
          </div>
          <div>
            <h3>What you get</h3>
            <p>${skill.output}</p>
          </div>
        </div>
      </article>`
      )
      .join("");

    list.addEventListener("click", (event) => {
      const button = event.target.closest(".skill-toggle");
      if (!button) return;
      const article = button.closest(".skill");
      const open = article.classList.toggle("open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".tab").forEach((tab) => {
    tab.addEventListener("click", () => {
      const id = tab.dataset.tab;
      document.querySelectorAll(".tab").forEach((el) => {
        el.classList.toggle("active", el === tab);
        el.setAttribute("aria-selected", el === tab ? "true" : "false");
      });
      document.querySelectorAll(".tab-panel").forEach((panel) => {
        panel.classList.toggle("active", panel.dataset.panel === id);
      });
    });
  });

  const header = document.querySelector(".site-header");
  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("scrolled", window.scrollY > 8);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
})();
