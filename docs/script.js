(function () {
  const skills = window.UNDERWRITER_SKILLS || [];
  const list = document.getElementById("skill-list");
  const filters = document.getElementById("pack-filters");
  let activePack = "all";

  const packLabels = {
    all: "All",
    knowledge: "Knowledge",
    underwriting: "Underwriting",
    claims: "Claims",
    customer: "Customer",
    "personal-lines": "Personal lines",
    compliance: "Compliance",
    analytics: "Analytics",
  };

  const packs = ["all", ...new Set(skills.map((s) => s.pack))];

  function renderFilters() {
    if (!filters) return;
    filters.innerHTML = packs
      .map(
        (pack) => `
      <button type="button" class="pack-chip ${pack === activePack ? "active" : ""}" data-pack="${pack}">
        ${packLabels[pack] || pack}
      </button>`
      )
      .join("");
  }

  function renderSkills() {
    if (!list) return;
    const visible = skills.filter((s) => activePack === "all" || s.pack === activePack);
    list.innerHTML = visible
      .map(
        (skill, index) => `
      <article class="skill" data-skill="${skill.id}" style="animation-delay: ${index * 20}ms">
        <button class="skill-toggle" type="button" aria-expanded="false">
          <span>
            <span class="skill-pack">${packLabels[skill.pack] || skill.pack}</span>
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
  }

  renderFilters();
  renderSkills();

  filters?.addEventListener("click", (event) => {
    const chip = event.target.closest(".pack-chip");
    if (!chip) return;
    activePack = chip.dataset.pack;
    renderFilters();
    renderSkills();
  });

  list?.addEventListener("click", (event) => {
    const button = event.target.closest(".skill-toggle");
    if (!button) return;
    const article = button.closest(".skill");
    const open = article.classList.toggle("open");
    button.setAttribute("aria-expanded", open ? "true" : "false");
  });

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
  const onScroll = () => header?.classList.toggle("scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
})();
