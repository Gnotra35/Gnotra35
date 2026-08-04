"""
Verified, hand-curated facts for the profile dashboard.
"""

OWNER = "payal-35"
NAME = "Payal Gnotra"
TAGLINE = "Full Stack Web Developer (Golang & React)"
SUBLINE = "I build distributed systems, scalable microservices, and user-friendly interfaces."

# ---------------------------------------------------------------------------
# The flagship portfolio.
# ---------------------------------------------------------------------------
FLAGSHIPS = [
    # Backend & Distributed Systems
    dict(name="grc-distributed-monolith", domain="Backend & Systems", lang="Go", tag="v1.0.0",
         blurb="Production-grade distributed system with 10+ independently deployable services, strongly-typed gRPC, NATS event queues, and Kong API Gateway."),
    
    # Full Stack Development
    dict(name="form-engine", domain="Full Stack Development", lang="JavaScript", tag=None,
         blurb="Full-stack dynamic engine for ID card printing with a schema-driven React renderer and dual-side validation."),
    
    # Tooling & Automation
    dict(name="automated-installer", domain="Automation", lang="Go", tag="v1.2",
         blurb="One-command deployment toolchain for environment setup and service bootstrapping on fresh machines."),
    
    # Security
    dict(name="CompliSec", domain="Security", lang="Shell", tag="v1.0",
         blurb="Automated Vulnerability Scanning Tool with Basic, Intermediate, and Advanced scanning modes. Built at Yukti Sangam Hackathon 2025."),
    
    # Mobile Development
    dict(name="flutter-ui-kit", domain="Mobile Development", lang="Dart", tag=None,
         blurb="Reusable, performant Flutter components and responsive layouts for cross-platform mobile applications."),
]

DOMAINS = [
    "Backend & Systems",
    "Full Stack Development",
    "Automation",
    "Security",
    "Mobile Development",
]

# ---------------------------------------------------------------------------
# Verified benchmark numbers.
# ---------------------------------------------------------------------------
BENCHMARKS = [
    dict(repo="grc-distributed-monolith", metric="gRPC overhead vs REST",
         value="-30%", detail="Reduced serialization overhead by 30% using strongly-typed gRPC",
         env="Golang · Microservices", source="Internal Benchmarks",
         bar=0.30),
    dict(repo="form-engine", metric="turnaround time",
         value="-80%", detail="Reduced turnaround time by 80% for non-technical users via schema-driven renderer",
         env="React · PostgreSQL", source="User Analytics",
         bar=0.80),
    dict(repo="automated-installer", metric="onboarding time",
         value="-70%", detail="Reduced developer onboarding time by 70%",
         env="Golang · ElectronJS", source="Team Metrics",
         bar=0.70),
    dict(repo="rnr-microservices", metric="inter-service efficiency",
         value="+35%", detail="Improved communication efficiency by 35% using NATS event-driven patterns",
         env="Golang · NATS JetStream", source="Production Metrics",
         bar=0.35), 
]

# ---------------------------------------------------------------------------
# Regulatory / Roadmap Deadlines
# ---------------------------------------------------------------------------
PQC_DEADLINES = [
    dict(date="2026-10-01", label="Kubernetes & Service Mesh",
         note="Migrate production microservices to K8s with Helm charts and Istio"),
    dict(date="2027-02-01", label="Open Source Kits",
         note="Publish Golang microservices starter kit (gRPC, NATS, Kong)"),
    dict(date="2028-01-01", label="DevSecOps & Observability",
         note="Integrate automated security scanning and full observability stack (OpenTelemetry)"),
    dict(date="2030-01-01", label="Enterprise Architecture",
         note="Architect high-availability systems handling millions of users globally"),
]

# GitHub linguist colors
LANG_COLORS = {
    "JavaScript": "#f1e05a", "TypeScript": "#3178c6", "Python": "#3572A5",
    "Dart": "#00B4AB", "HTML": "#e34c26", "CSS": "#563d7c", "Go": "#00ADD8",
    "Java": "#b07219", "Shell": "#89e051"
}

# ===========================================================================
# Real professional background
# ===========================================================================

JOURNEY_ERAS = [
    dict(key="2021", label="FOUNDATIONS", accent="cyan",
         note="B.Tech CS begins — The software engineering journey starts"),
    dict(key="2023", label="FIRST BUILDS", accent="blue",
         note="Learning core web technologies, frontend frameworks, and backend basics"),
    dict(key="2024", label="MERN STACK", accent="purple",
         note="Mastering React, Node.js, and completing web development internships"),
    dict(key="2025", label="BUILD & SHIP", accent="orange",
         note="Hackathons, CompliSec, and deep dive into distributed systems"),
    dict(key="2026", label="FULL STACK PRO", accent="red",
         note="Working as Full Stack Developer at RNR Consulting Pvt. Ltd."),
]

JOURNEY_MILES = [
    dict(date="2021-05", label="Class XII", sub="Meritorious School Gurdaspur", lane="down", accent="cyan"),
    dict(date="2021-09", label="B.Tech CS begins", sub="Eternal University", lane="down", accent="cyan"),
    dict(date="2023-11", label="First UIs", sub="Learning Web Technologies", lane="up", accent="blue"),
    dict(date="2024-03", label="UX Design Cert", sub="Google Certified", lane="down", accent="purple"),
    dict(date="2024-05", label="SQL Cert", sub="HackerRank SQL Expert", lane="down", accent="purple"),
    dict(date="2024-12", label="Web Dev Intern", sub="Scout and Guide Trust India", lane="up", accent="orange"),
    dict(date="2025-01", label="Form Engine", sub="React & Golang platform", lane="up", accent="orange"),
    dict(date="2025-04", label="Yukti Sangam", sub="Hackathon 2025 Participant", lane="down", accent="orange"),
    dict(date="2025-07", label="CompliSec", sub="Automated Vuln Scanner", lane="up", accent="orange"),
    dict(date="2025-04", label="Full Stack Dev", sub="RNR Consulting", lane="up", accent="red"),
    dict(date="2026-06", label="Distributed Systems", sub="Golang & gRPC architecture", lane="up", accent="red"),
]

PUBLICATIONS = dict(
    counts=[("1+", "YEARS", "Production Experience"),
            ("10+", "PROJECTS", "Distributed Systems & Full Stack"),
            ("3", "CERTIFICATIONS", "2024-2025")],
    venues=[
        "Full Stack Developer @ RNR Consulting Pvt. Ltd. (Apr 2025 - Present)",
        "Web Developer Intern @ Scout and Guide Trust India (Dec 2024 - Feb 2025)",
        "Yukti Sangam Hackathon 2025 Participant - Built CompliSec",
        "Certifications: UX Design (Google), SQL (HackerRank)"
    ],
)

IMPACT = [
    ("35%", "Efficiency Boost", "Improved inter-service communication efficiency via NATS JetStream"),
    ("100%", "Secure Traffic", "Managed external service traffic using Kong API Gateway and JWT"),
    ("80%", "Faster Rendering", "Reduced turnaround time for non-technical users via schema-driven engine"),
    ("70%", "Onboarding", "Reduced developer setup time with Automated Installer"),
]

EARLIER = [
    dict(name="Old-Portfolio", year="2023", lang="HTML/CSS",
         blurb="Early version of my portfolio exploring basic web development concepts."),
]

CAREER_LINE = "Full Stack Developer @ RNR Consulting · B.Tech CS — Eternal University, 2021–25"
