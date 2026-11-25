"""
Applies the agreed updates to your portfolio's index.html.

Usage (from the folder that contains index.html):
    python update_portfolio.py

It makes a backup (index.html.bak) and only writes the file if EVERY change
found its anchor. If something doesn't match, it lists what failed and
leaves index.html untouched.
"""
import re
import shutil
import sys

SRC = "index.html"
s = open(SRC, encoding="utf-8").read()
fails = []
done = 0

def rep(old, new):
    global s, done
    if old not in s:
        fails.append(old[:70].replace("\n", " "))
        return
    s = s.replace(old, new)
    done += 1


def block(start, end, new):
    """Replace everything from `start` up to (not including) `end`."""
    global s, done
    i, j = s.find(start), s.find(end)
    if i < 0 or j < 0 or j < i:
        fails.append("block: " + start)
        return
    s = s[:i] + new + s[j:]
    done += 1


# ---------------------------------------------------------------- head / SEO
rep("<title>Roshan Varghese | AI Engineer — RAG, Multi-Agent Systems & Applied ML</title>",
    "<title>Roshan Varghese | Data &amp; AI Engineer — RAG, Multi-Agent Systems &amp; Data Engineering</title>")
rep("an AI Engineer specializing in RAG pipelines, multi-agent LLM systems, and applied ML, with a data engineering background from Deloitte",
    "a Data &amp; AI Engineer building RAG pipelines, multi-agent LLM systems, and applied ML, with 2 years of data/ETL engineering at Deloitte")
rep('content="Roshan Varghese, AI Engineer, RAG,',
    'content="Roshan Varghese, Data &amp; AI Engineer, Data Engineer, ETL, SQL, RAG,')
rep('content="Roshan Varghese | AI Engineer"',
    'content="Roshan Varghese | Data &amp; AI Engineer"')
rep("RAG pipelines, multi-agent LLM systems, and applied ML — bridging AI research and production-grade engineering.",
    "Data &amp; AI engineer: RAG pipelines, multi-agent LLM systems, and applied ML, built on a data engineering foundation.")

# ---------------------------------------------------------------- hero / nav
rep('<span class="nav-drawer-role">AI Engineer</span>',
    '<span class="nav-drawer-role">Data &amp; AI Engineer</span>')
rep('<div class="hero-label">AI Engineer</div>',
    '<div class="hero-label">Data &amp; AI Engineer</div>')
rep("Bridging the gap between cutting-edge AI research and real-world applications through RAG pipelines, multi-agent systems, and applied ML.",
    "From reliable data to working AI: RAG pipelines, multi-agent systems, and applied ML, built on a data engineering foundation.")
rep("bringing production-grade reliability discipline to AI system design.",
    "bringing production-grade reliability discipline to AI system design. AWS Certified AI Practitioner.")
rep('<a href="#projects" class="btn btn-secondary">View Projects</a>',
    '<a href="#projects" class="btn btn-secondary">View Projects</a>\n'
    '                    <a href="Roshan_Varghese_Resume.pdf" class="btn btn-secondary" download>Download Resume</a>\n'
    '                    <p class="hero-availability">Open to data engineering, data analyst and AI/ML roles · Bengaluru · Remote / Hybrid</p>')
rep("</style>", """        .hero-availability {
            flex-basis: 100%;
            margin-top: 14px;
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--navy-primary);
        }
    </style>""")

# ---------------------------------------------------------------- experience
EXPERIENCE = r'''<!-- Experience Section -->
    <section id="experience">
        <div class="section-header">
            <div class="section-number" aria-hidden="true">01</div>
            <div class="section-label">Career Journey</div>
            <h2 class="section-title">Work Experience</h2>
            <p class="section-description">
                Professional journey spanning AI/ML engineering and data engineering across an AI-focused startup and a global consulting firm.
            </p>
        </div>
        
        <div class="experience-timeline">
            <div class="experience-item">
                <div class="experience-header">
                    <div>
                        <h3 class="experience-title">Vision AI Intern</h3>
                        <div class="experience-company">Codexoho Digitals Pvt Ltd, Bangalore</div>
                    </div>
                    <div class="experience-date">February 2026 – March 2026</div>
                </div>
                <ul class="experience-list">
                    <li>Integrated and tuned the AI pipeline for a near-real-time facial-recognition attendance and visitor-management system (2-person team): YOLOv8-Face detection, BoT-SORT tracking and AdaFace IR50 embeddings matched against an employee gallery in PostgreSQL by cosine similarity, with a tuned threshold, a liveness check added after mannequins were detected as people, and a 4-attempt limit before classifying someone as a visitor</li>
                    <li>Built the FastAPI REST/WebSocket backend, an 11-table PostgreSQL schema (SQLAlchemy) and JWT role-based access; deployed on a VPS with Docker, MediaMTX and Tailscale-tunneled RTSP for a 2-camera, 37-employee pilot, alongside a Next.js/React dashboard built mainly by my teammate</li>
                    <li>Identified 8 of 10 employees (80%) in a recorded-video test and 6 of 10 (60%) in a live CPU test; cut average per-frame latency from &gt;2s to &lt;500ms by running AdaFace only on new tracks, passing AdaFace embeddings into BoT-SORT and lowering YOLO input resolution</li>
                    <li>Experimented with quantization and batching on a local GPU machine and compared GPU vs CPU in Colab to recommend an RTX 4090 for scaling toward 40 cameras</li>
                </ul>
            </div>

            <div class="experience-item">
                <div class="experience-header">
                    <div>
                        <h3 class="experience-title">AI Developer Intern</h3>
                        <div class="experience-company">KOTS Daily Services Pvt Ltd, Bangalore</div>
                    </div>
                    <div class="experience-date">April 2025 – October 2025</div>
                </div>
                <ul class="experience-list">
                    <li>Designed a decentralized 3-agent LangChain/Google ADK workflow (Jira, Calendar/Notion, Knowledge) with a FastAPI orchestration layer and role-based access control, automating a multi-step enterprise process (retrieval, routing, response generation) as a proof-of-concept; moved from a centralized design to remove a single point of failure</li>
                    <li>Improved contextual answer relevance by building and evaluating a RAG pipeline (FAISS vector database, Google Gemini embeddings) over PDFs and chat history, benchmarking retrieval quality against labeled queries and tracing queries with LangSmith to track token usage and response time</li>
                    <li>Fixed a context-memory bug that made agents re-request details after 5 conversation turns</li>
                    <li>Explored low-code agent creation patterns to simplify how non-technical users could configure and deploy custom agents within the POC ecosystem</li>
                    <li>Prototyped orchestration patterns for coordinating multiple specialized AI agents toward a shared task</li>
                </ul>
            </div>
            
            <div class="experience-item">
                <div class="experience-header">
                    <div>
                        <h3 class="experience-title">Associate Analyst – Data/ETL Engineering</h3>
                        <div class="experience-company">Deloitte Consulting USI, Bangalore</div>
                    </div>
                    <div class="experience-date">August 2022 – June 2024</div>
                </div>
                <ul class="experience-list">
                    <li>Tested 80+ SAP BI reports to confirm data populated accurately, and validated 184+ Pentaho ETL jobs and the reports they generated in the healthcare domain, reviewing SQL (stored procedures, DML, DDL) for correctness and raising issues with root-cause analyses</li>
                    <li>Root-caused 5 critical ETL/SQL issues assigned through Jira, including a data-integrity defect undetected for 3–4 years in 2 ETL jobs; rebuilt the jobs, tested them in a sandbox and promoted them through dev and UAT to production only after each stage passed, reprocessing historical data so reports were accurate</li>
                    <li>Built a proof-of-concept PDF validator to automate format checks on generated reports — foundational data-reliability experience now applied to validating AI/RAG pipeline outputs</li>
                </ul>
            </div>
        </div>
    </section>
    
    '''
block("<!-- Experience Section -->", "<!-- Projects Section -->", EXPERIENCE)

# ---------------------------------------------------------------- projects
rep('<div class="project-date">March 2026 · Completed</div>',
    '<div class="project-date">February – March 2026 · Completed</div>')
rep("cited answers, with multi-provider LLM support (Gemini, OpenAI, Groq) and configurable response modes.",
    "cited answers, with multi-provider LLM support (Gemini, OpenAI, Groq) and configurable response modes. "
    "Indexes 10 government scheme documents; evaluated on 25+ test queries at 2–4s response time.")
rep("Jul – Nov 2025 · Presented at WCSC 2026", "Jul – Oct 2025 · Presented at WCSC 2026")
rep("14-class pest detection CV model. Co-authored paper,",
    "14-class pest detection CV model, reaching a 90% query success rate (36/40) at 2.94s average latency. Co-authored paper,")
rep('<span class="tag">Published Research</span>', '<span class="tag">Presented at WCSC 2026</span>')

# ---------------------------------------------------------------- skills
def add_after(anchor, items):
    extra = "".join('\n                    <div class="skill-item">%s</div>' % i for i in items)
    rep(anchor, anchor + extra)

add_after('<div class="skill-item">Prompt Engineering</div>',
          ["Claude Code", "GitHub Copilot", "LangSmith", "Groq"])
add_after('<div class="skill-item">TensorFlow</div>',
          ["PyTorch", "scikit-learn", "NumPy", "Prophet / ARIMA", "YOLOv8-Face", "BoT-SORT", "AdaFace", "MediaPipe"])
add_after('<div class="skill-item">REST APIs</div>',
          ["WebSockets", "JWT", "SQLAlchemy", "Pydantic", "pytest"])
add_after('<div class="skill-item">Tailscale</div>', ["AWS Amplify"])
rep('<div class="skill-item">Informatica</div>', '<div class="skill-item">Informatica (training)</div>')
rep('<div class="skill-item">Power BI</div>', '<div class="skill-item">Power BI (training)</div>')

# ---------------------------------------------------------------- contact
rep("Open to discussing new opportunities, collaborations, and AI engineering roles.",
    "Open to discussing new opportunities, collaborations, and data and AI engineering roles.")
s, n = re.subn(r'\s*<li class="contact-item">\s*<div class="contact-label">Phone</div>.*?</li>', "", s, count=1, flags=re.S)
if n == 1:
    done += 1
else:
    fails.append("phone block")

# ---------------------------------------------------------------- write
if fails:
    print("NOT WRITTEN. These changes could not find their place:")
    for f in fails:
        print("  -", f)
    sys.exit(1)

shutil.copyfile(SRC, SRC + ".bak")
open(SRC, "w", encoding="utf-8").write(s)
print("Done: %d changes applied. Backup saved as index.html.bak" % done)