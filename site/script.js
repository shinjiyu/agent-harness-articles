(() => {
  const chapters = window.AH_CONTENT || [];
  const meta = window.AH_META || {};
  const sidebar = document.getElementById("sidebar");
  const article = document.getElementById("chapter");
  const search = document.getElementById("search");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const menuToggle = document.getElementById("menuToggle");
  const overlay = document.getElementById("overlay");
  const stamp = document.getElementById("buildStamp");

  let currentId = "home";

  if (stamp && meta.paper_counts) {
    const c = meta.paper_counts;
    stamp.textContent = `论文 ${c.total} · A${c.A}/B${c.B}/C${c.C}`;
    stamp.title = `index updated_at: ${meta.built_from_index_updated_at || ""}`;
  }

  function buildNav(filter = "") {
    const q = filter.trim().toLowerCase();
    sidebar.innerHTML = "";
    let lastModule = null;
    let moduleWrap = null;

    chapters.forEach((ch) => {
      const hay = `${ch.title} ${ch.keywords || ""} ${ch.module}`.toLowerCase();
      const show = !q || hay.includes(q);
      if (ch.module !== lastModule) {
        lastModule = ch.module;
        moduleWrap = document.createElement("div");
        moduleWrap.className = "nav-module";
        const title = document.createElement("div");
        title.className = "nav-module-title";
        title.textContent = ch.module;
        moduleWrap.appendChild(title);
        sidebar.appendChild(moduleWrap);
      }
      const a = document.createElement("a");
      a.className = "nav-link" + (show ? "" : " hidden");
      a.href = `#${ch.id}`;
      a.dataset.id = ch.id;
      a.textContent = ch.title;
      if (ch.id === currentId) a.classList.add("active");
      a.addEventListener("click", () => closeMobile());
      moduleWrap.appendChild(a);
    });
  }

  function findIndex(id) {
    return chapters.findIndex((c) => c.id === id);
  }

  function render(id) {
    const idx = findIndex(id);
    const ch = chapters[idx] || chapters[0];
    if (!ch) return;
    currentId = ch.id;
    article.innerHTML = ch.html;
    document.title = `${ch.title} — Agent Harness 知识库`;
    buildNav(search.value);
    prevBtn.disabled = idx <= 0;
    nextBtn.disabled = idx >= chapters.length - 1;
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function go(delta) {
    const idx = findIndex(currentId);
    const next = chapters[idx + delta];
    if (!next) return;
    location.hash = next.id;
  }

  function closeMobile() {
    sidebar.classList.remove("open");
    overlay.hidden = true;
  }

  function openMobile() {
    sidebar.classList.add("open");
    overlay.hidden = false;
  }

  prevBtn.addEventListener("click", () => go(-1));
  nextBtn.addEventListener("click", () => go(1));
  search.addEventListener("input", () => buildNav(search.value));
  menuToggle.addEventListener("click", () => {
    if (sidebar.classList.contains("open")) closeMobile();
    else openMobile();
  });
  overlay.addEventListener("click", closeMobile);

  window.addEventListener("hashchange", () => {
    const id = location.hash.replace(/^#/, "") || "home";
    render(id);
  });

  const initial = location.hash.replace(/^#/, "") || "home";
  render(initial);
})();
