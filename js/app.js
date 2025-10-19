// UI logic only. Imports data from data.js.
}


function updateChartTheme() {
if (!skillsRadarChart) {
renderChart();
} else {
const cfg = getChartConfig();
skillsRadarChart.data = cfg.data;
skillsRadarChart.options = cfg.options;
skillsRadarChart.update();
}
}


function updateLanguage(lang) {
currentLang = lang;
document.documentElement.lang = lang;
const languageToggleBtn = qs('#language-toggle');
if (languageToggleBtn)
languageToggleBtn.textContent = lang === 'fr' ? 'EN' : 'FR';
localStorage.setItem('language', lang);


setTextByLangKeys(lang);
renderEducation(lang);
renderCertifications(lang);
renderTimeline(lang);
updateChartTheme();
}


function initTheme() {
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const stored = localStorage.getItem('color-theme');
const isDark = stored ? stored === 'dark' : prefersDark;
document.documentElement.classList.toggle('dark', isDark);
}


function bindListeners() {
const themeToggleBtn = qs('#theme-toggle');
if (themeToggleBtn) {
themeToggleBtn.addEventListener('click', () => {
document.documentElement.classList.toggle('dark');
localStorage.setItem(
'color-theme',
document.documentElement.classList.contains('dark') ? 'dark' : 'light'
);
updateChartTheme();
});
}


const languageToggleBtn = qs('#language-toggle');
if (languageToggleBtn) {
languageToggleBtn.addEventListener('click', () => {
const newLang = currentLang === 'fr' ? 'en' : 'fr';
updateLanguage(newLang);
});
}
}


function init() {
initTheme();
const savedLang = localStorage.getItem('language') || DEFAULT_LANG;
updateLanguage(savedLang);
renderChart();
bindListeners();
}


// Bootstrap on DOM ready
if (document.readyState === 'loading') {
document.addEventListener('DOMContentLoaded', init);
} else {
init();
}
