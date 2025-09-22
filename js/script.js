document.addEventListener('DOMContentLoaded', function () {
            const themeToggleBtn = document.getElementById('theme-toggle');
            const languageToggleBtn = document.getElementById('language-toggle');
            let skillsRadarChart;
            let currentLang = 'fr';

            const translations = {
                fr: {
                    jobTitle: "Concepteur Développeur Data IA",
                    profileDescription: "Développeur agile et proactif avec une solide expertise en développement applicatif Python et une passion pour la transformation des données en solutions intelligentes. Mon parcours, de la chimie analytique au développement web, m'a doté d'une rigueur scientifique et d'une grande capacité d'adaptation.",
                    portfolioLink: "Portfolio/GitHub",
                    location: "Strasbourg & Full Remote",
                    skillsTitle: "Compétences",
                    skillsDescription: "Cette visualisation représente mes domaines de compétences clés pour un futur poste d'Ingénieur IA. Chaque axe montre une compétence fondamentale, et l'étendue de la zone colorée indique mon niveau de maîtrise. Survolez les points pour plus de détails.",
                    educationTitle: "Formation & Diplômes",
                    educationDescription: "Mon parcours académique, alliant la rigueur scientifique à l'expertise technique en développement.",
                    certificationsTitle: "Certifications",
                    certificationsDescription: "Mes certifications attestent de mes compétences techniques et de mon engagement dans le domaine de la Data et de l'IA.",
                    certifications: [
                        { title: "Certificat Professionnel Développeur IA par IBM", provider: "Coursera", date: "2025", link: "https://www.credly.com/badges/89dc6e8c-2f73-483b-91d8-0501fb11790d" },
                        { title: "Programmation Python 3 par l'Université du Michigan", provider: "Coursera", date: "2023", link: "https://www.coursera.org/account/accomplishments/specialization/6FETXJVPRGWS" },
                        { title: "Python : Un Voyage Guidé de l'Introduction à l'Application par l'Université d'Arizona", provider: "Coursera", date: "2025", link: "https://www.coursera.org/account/accomplishments/specialization/82TNMGS3LMBQ" },
                        { title: "Calcul Différentiel à travers les Données et la Modélisation par l'Université Johns Hopkins", provider: "Coursera", date: "2025", link: "https://www.coursera.org/account/accomplishments/specialization/7JFXXS0NZKYM" },
                        { title: "Calcul Intégral à travers les Données et la Modélisation par l'Université Johns Hopkins", provider: "Coursera", date: "2025", link: "https://coursera.org/share/bbe0e1d85f0966dbe0f8b781b2b4d01b" },
                        { title: "Autoroute vers la Science des Données : Mathématiques Essentielles par l'Université du Colorado Boulder", provider: "Coursera", date: "2023", link: "https://www.coursera.org/account/accomplishments/specialization/MBEWSA8BGJAH" }
                    ],
                    experienceTitle: "Parcours Professionnel",
                    experienceDescription: "Mon parcours est une suite logique d'expériences qui m'ont mené vers la Data et l'IA. Cliquez sur chaque étape pour découvrir les missions et les compétences que j'y ai développées.",
                    contactTitle: "Contact",
                    contactDescription: "Prêt à discuter de mon profil et de vos opportunités d'alternance pour 2025:",
                    rqthStatus: "Statut de Travailleur Handicapé (RQTH)",
                    chartLegend: "Niveau de Maîtrise",
                    chartLabels: ['Développement Python (Flask/Django)', 'Gestion de Données (SQL/ORM)', 'Méthodologie Agile (SCRUM)', 'Versioning (Git)', 'Architecture (UML)', 'Développement Web (JS/HTML/CSS)'],
                    education: [
                        { degree: "Bachelor Développeur d'Applications Python", institution: "Studi", period: "Juin 2023 - Mars 2024", location: "En ligne" },
                        { degree: "DUT Chimie", institution: "Université de Strasbourg", period: "Septembre 1997 - Juillet 1999", location: "Strasbourg" }
                    ],
                    experiences: [
                        { year: '2013 - 2017', title: 'Créateur de Contenu Multimédia & Cofondateur', company: 'Association Colibulle', description: 'Développement web (WordPress, HTML, CSS), gestion de projet, gestion administrative et communication. Création de supports pédagogiques et animation d\'interventions publiques.' },
                        { year: '2012 - 2013', title: 'Assistant Informatique', company: 'Association Vetis', description: 'Audit et optimisation de la sécurité du réseau local. Veille technologique et maintenance du parc informatique.' },
                        { year: '2003 - 2009', title: 'Intervenant de Soutien Scolaire (Indépendant)', company: 'Strasbourg', description: 'Vulgarisation de concepts complexes en mathématiques et sciences physiques. Développement d\'une forte compétence pédagogique.' },
                        { year: '1999 - 2002', title: 'Technicien en Chimie Analytique', company: 'Laboratoires Roche, IReS, ECPM', description: 'Application de protocoles d\'analyse stricts, garantissant la précision et la fiabilité des résultats. Acquisition d\'une méthodologie de travail rigoureuse et d\'un esprit analytique aiguisé.' }
                    ]
                },
                en: {
                    jobTitle: "Data AI Developer",
                    profileDescription: "Agile and proactive developer with solid expertise in Python application development and a passion for transforming data into intelligent solutions. My journey from analytical chemistry to web development has equipped me with scientific rigor and great adaptability.",
                    portfolioLink: "Portfolio/GitHub",
                    location: "Strasbourg & Full Remote",
                    skillsTitle: "Skills",
                    skillsDescription: "This visualization represents my key skill areas for an AI Engineer position. Each axis shows a fundamental skill, and the extent of the colored area indicates my level of mastery. Hover over the points for more details.",
                    educationTitle: "Education & Degrees",
                    educationDescription: "My academic background, combining scientific rigor with technical expertise in development.",
                    certificationsTitle: "Certifications",
                    certificationsDescription: "My certifications attest to my technical skills and commitment in the field of Data and AI.",
                    certifications: [
                        { title: "IBM AI Developer Professional Certificate", provider: "Coursera", date: "2025", link: "https://www.credly.com/badges/89dc6e8c-2f73-483b-91d8-0501fb11790d" },
                        { title: "Python 3 Programming by University of Michigan", provider: "Coursera", date: "2023", link: "https://www.coursera.org/account/accomplishments/specialization/6FETXJVPRGWS" },
                        { title: "Python: A Guided Journey from Introduction to Application by Arizona State University", provider: "Coursera", date: "2025", link: "https://www.coursera.org/account/accomplishments/specialization/82TNMGS3LMBQ" },
                        { title: "Differential Calculus through Data and Modeling by Johns Hopkins University ", provider: "Coursera", date: "2025", link: "https://www.coursera.org/account/accomplishments/specialization/7JFXXS0NZKYM" },
                        { title: "Integral Calculus through Data and Modeling by Johns Hopkins University ", provider: "Coursera", date: "2025", link: "https://coursera.org/share/bbe0e1d85f0966dbe0f8b781b2b4d01b" },        
                        { title: "Expressway to Data Science: Essential Math by University of Colorado Boulder", provider: "Coursera", date: "2023", link: "https://www.coursera.org/account/accomplishments/specialization/MBEWSA8BGJAH" }
                    ],
                    experienceTitle: "Career Path",
                    experienceDescription: "My career is a logical sequence of experiences that have led me to Data and AI. Click on each step to discover the missions and skills I developed there.",
                    contactTitle: "Contact",
                    contactDescription: "Ready to discuss my profile and your apprenticeship opportunities for 2025:",
                    rqthStatus: "Disability Status (RQTH)",
                    chartLegend: "Mastery Level",
                    chartLabels: ['Python Development (Flask/Django)', 'Data Management (SQL/ORM)', 'Agile Methodology (SCRUM)', 'Versioning (Git)', 'Architecture (UML)', 'Web Development (JS/HTML/CSS)'],
                    education: [
                        { degree: "Bachelor's Degree in Python Application Development", institution: "Studi", period: "June 2023 - March 2024", location: "Online" },
                        { degree: "University Diploma in Chemistry", institution: "University of Strasbourg", period: "September 1997 - July 1999", location: "Strasbourg" }
                    ],
                    experiences: [
                        { year: '2013 - 2017', title: 'Multimedia Content Creator & Co-founder', company: 'Colibulle Association', description: 'Web development (WordPress, HTML, CSS), project management, administrative and organizational management. Creation of educational materials and animation of public interventions.' },
                        { year: '2012 - 2013', title: 'IT Assistant', company: 'Vetis Association', description: 'Audit and optimization of local network security. Technological watch and maintenance of the IT equipment.' },
                        { year: '2003 - 2009', title: 'Academic Support Tutor (Freelance)', company: 'Strasbourg', description: 'Simplifying complex concepts in mathematics and physical sciences. Development of strong pedagogical skills.' },
                        { year: '1999 - 2002', title: 'Analytical Chemistry Technician', company: 'Roche, IReS, ECPM Laboratories', description: 'Application of strict analysis protocols, ensuring the precision and reliability of results. Acquisition of a rigorous work methodology and a sharp analytical mind.' }
                    ]
                }
            };
            
            function updateLanguage(lang) {
                currentLang = lang;
                document.documentElement.lang = lang;
                languageToggleBtn.textContent = lang === 'fr' ? 'EN' : 'FR';
                localStorage.setItem('language', lang);

                document.querySelectorAll('[data-lang-key]').forEach(element => {
                    const key = element.getAttribute('data-lang-key');
                    if (translations[lang][key]) {
                        element.textContent = translations[lang][key];
                    }
                });
                
                renderEducation(lang);
                renderCertifications(lang);
                renderTimeline(lang);
                updateChartTheme();
            }

            function getChartOptions() {
                const isDarkMode = document.documentElement.classList.contains('dark');
                const lang = currentLang;
                
                const gridColor = isDarkMode ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)';
                const pointLabelColor = isDarkMode ? '#CBD5E1' : '#3D3D3D';
                const datasetColor = isDarkMode ? 'rgba(45, 212, 191, 1)' : 'rgba(13, 148, 136, 1)';
                const datasetBgColor = isDarkMode ? 'rgba(45, 212, 191, 0.2)' : 'rgba(13, 148, 136, 0.2)';

                return {
                    data: {
                        labels: translations[lang].chartLabels,
                        datasets: [{
                            label: translations[lang].chartLegend,
                            data: [85, 80, 90, 95, 75, 70],
                            backgroundColor: datasetBgColor,
                            borderColor: datasetColor,
                            pointBackgroundColor: datasetColor,
                            pointBorderColor: isDarkMode ? '#0F172A' : '#FFFFFF',
                            pointHoverBackgroundColor: isDarkMode ? '#0F172A' : '#FFFFFF',
                            pointHoverBorderColor: datasetColor
                        }]
                    },
                    options: {
                        responsive: true, maintainAspectRatio: false,
                        scales: { r: { angleLines: { color: gridColor }, grid: { color: gridColor }, pointLabels: { font: { size: 14 }, color: pointLabelColor }, ticks: { backdropColor: 'transparent', stepSize: 25, display: false }, suggestedMin: 0, suggestedMax: 100 }},
                        plugins: { legend: { display: false }, tooltip: { callbacks: { label: (c) => `${c.dataset.label}: ${c.parsed.r}%` }}}
                    }
                };
            }

            function renderChart() {
                if(skillsRadarChart) skillsRadarChart.destroy();
                const chartConfig = getChartOptions();
                const ctx = document.getElementById('skillsRadarChart').getContext('2d');
                skillsRadarChart = new Chart(ctx, { type: 'radar', data: chartConfig.data, options: chartConfig.options });
            }
            
            function updateChartTheme() {
                if (!skillsRadarChart) {
                    renderChart();
                } else {
                    const chartConfig = getChartOptions();
                    skillsRadarChart.data = chartConfig.data;
                    skillsRadarChart.options = chartConfig.options;
                    skillsRadarChart.update();
                }
            }
            
            function renderEducation(lang) {
                const educationContainer = document.getElementById('education-container');
                educationContainer.innerHTML = '';
                const educationItems = translations[lang].education;

                educationItems.forEach(item => {
                    const card = document.createElement('div');
                    card.className = "bg-white dark:bg-slate-800 p-6 rounded-lg shadow-md hover:shadow-lg dark:hover:shadow-teal-500/10 transition-all duration-300 flex flex-col";
                    card.innerHTML = `
                        <h3 class="text-lg font-bold text-teal-600 dark:text-teal-400">${item.degree}</h3>
                        <p class="font-semibold text-slate-700 dark:text-slate-200 mt-1">${item.institution}</p>
                        <div class="mt-auto pt-4">
                            <p class="text-sm text-slate-500 dark:text-slate-400">${item.period}</p>
                            <p class="text-sm text-slate-500 dark:text-slate-400">${item.location}</p>
                        </div>
                    `;
                    educationContainer.appendChild(card);
                });
            }

            function renderCertifications(lang) {
                const certificationsContainer = document.getElementById('certifications-container');
                certificationsContainer.innerHTML = '';
                const certifications = translations[lang].certifications;
                certifications.forEach(cert => {
                    const card = document.createElement('div');
                    card.className = "bg-white dark:bg-slate-800 p-6 rounded-lg shadow-md hover:shadow-lg dark:hover:shadow-teal-500/10 transition-all duration-300 flex flex-col";
                    card.innerHTML = `
                        <h3 class="text-lg font-bold text-teal-600 dark:text-teal-400">${cert.title}</h3>
                        <p class="font-semibold text-slate-700 dark:text-slate-200 mt-1">${cert.provider}</p>
                        <p class="text-sm text-slate-500 dark:text-slate-400 mt-2">${cert.date}</p>
                        ${cert.link ? `<a href="${cert.link}" target="_blank" class="mt-2 text-teal-500 dark:text-teal-400 hover:underline">Voir la certification</a>` : ''}
                    `;
                    certificationsContainer.appendChild(card);
                });
            }



            function renderTimeline(lang) {
                const timelineContainer = document.getElementById('timeline-container');
                timelineContainer.innerHTML = '';
                const experiences = translations[lang].experiences;

                experiences.forEach((exp, index) => {
                    const item = document.createElement('div');
                    item.className = `relative timeline-item`;
                    const alignmentClass = index % 2 === 0 ? 'md:pr-8' : 'md:pl-8';
                    const marginClass = index % 2 === 0 ? 'md:mr-auto' : 'md:ml-auto';
                    item.innerHTML = `
                        <div class="md:w-1/2 ${marginClass} ${alignmentClass} w-full">
                            <div class="cursor-pointer bg-white dark:bg-slate-800 p-4 rounded-lg shadow-md hover:shadow-lg dark:hover:shadow-teal-500/10 transition-all duration-300 timeline-item-header">
                                <div class="flex justify-between items-center">
                                    <div>
                                        <p class="font-bold text-teal-600 dark:text-teal-400">${exp.year}</p>
                                        <h3 class="font-semibold text-lg text-slate-800 dark:text-slate-100">${exp.title}</h3>
                                        <p class="text-sm text-slate-500 dark:text-slate-400">${exp.company}</p>
                                    </div>
                                    <div class="w-6 h-6 bg-teal-500 rounded-full flex items-center justify-center text-white font-bold text-sm transition-transform duration-300 transform chevron">
                                        <span>+</span>
                                    </div>
                                </div>
                            </div>
                            <div class="bg-slate-100 dark:bg-slate-800/70 rounded-b-lg timeline-item-content">
                                <p class="text-slate-600 dark:text-slate-300 text-sm">${exp.description}</p>
                            </div>
                        </div>
                    `;
                    timelineContainer.appendChild(item);
                });

                document.querySelectorAll('.timeline-item-header').forEach(header => {
                    header.addEventListener('click', () => {
                        const content = header.nextElementSibling;
                        const chevron = header.querySelector('.chevron span');
                        const wasActive = content.classList.contains('active');
                        
                        document.querySelectorAll('.timeline-item-content.active').forEach(openContent => {
                            openContent.classList.remove('active');
                            const otherChevron = openContent.previousElementSibling.querySelector('.chevron span');
                            otherChevron.textContent = '+';
                            otherChevron.parentElement.classList.remove('rotate-45');
                        });
                        
                        if(!wasActive) {
                            content.classList.add('active');
                            chevron.textContent = '-';
                            chevron.parentElement.classList.add('rotate-45');
                        }
                    });
                });
            }
            
            // --- Initialisation ---
            function init() {
                // Thème
                if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                    document.documentElement.classList.add('dark');
                } else {
                    document.documentElement.classList.remove('dark');
                }
                
                // Langue
                const savedLang = localStorage.getItem('language') || 'fr';
                updateLanguage(savedLang);

                // Listeners
                themeToggleBtn.addEventListener('click', () => {
                    document.documentElement.classList.toggle('dark');
                    localStorage.setItem('color-theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
                    updateChartTheme();
                });

                languageToggleBtn.addEventListener('click', () => {
                    const newLang = currentLang === 'fr' ? 'en' : 'fr';
                    updateLanguage(newLang);
                });
            }

            init();

        });

