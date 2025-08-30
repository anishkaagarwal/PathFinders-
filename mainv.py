
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
st.markdown(
	"""
	<style>
	body {
		background-color: #181920;
	}
	.main {
		background: #181920;
	}
	.gradient-header {
		background: linear-gradient(90deg, #ff6a00, #ee0979);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		font-size: 2.5rem;
		font-weight: 700;
		text-align: center;
		margin-bottom: 0.5em;
	}
	.section-title {
		color: #00bfff;
		font-size: 1.2rem;
		font-weight: 600;
		margin-bottom: 0.5em;
	}
	.stTextInput>div>input {
		background: #23243a;
		color: #fff;
		border-radius: 8px;
		border: 1px solid #444;
	}
	.stButton>button {
		background: linear-gradient(90deg, #ff6a00, #ee0979);
		color: #fff;
		font-weight: 600;
		border-radius: 8px;
		border: none;
		padding: 0.6em 1.2em;
		box-shadow: 0 2px 8px rgba(255,106,0,0.15);
		transition: transform 0.1s;
	}
	.stButton>button:hover {
		transform: scale(1.05);
		box-shadow: 0 4px 16px rgba(238,9,121,0.18);
	}
	.emoji {
		font-size: 1.5rem;
		margin-right: 0.3em;
	}
	</style>
	""",
	unsafe_allow_html=True
)

st.markdown('<div class="gradient-header">🚀👩‍💼🧑‍💼🤔❓📘<br>PathFinder: Your Career Counsellor Bot</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center;"><span style="color:#ffd700;font-size:1.1rem;">Hey there 🚀! <b>PathFinder</b> is your AI bestie for career glow-ups.<br>Ready to vibe with your future? Let\'s unlock 🔓 your dream job in the coolest, fastest-growing fields!<br>Drop your skills, passions, and goals below and let\'s get you trending. 💡✨</span></div>', unsafe_allow_html=True)



# Only render the glass-box for the
st.markdown('<div class="section-title">📝 Fill in your details:</div>', unsafe_allow_html=True)
with st.form("career_form"):
	name = st.text_input("🧑‍💼 Your Name:")
	strengths = st.text_input("💪 Your Strengths (e.g., coding, problem solving, creative):")
	weaknesses = st.text_input("🌿 Your Weaknesses (optional):")
	interests = st.text_input("🧠 Your Interests (e.g., data, art, leadership):")
	work_style = st.text_input("🏢 Preferred Work Style (e.g., remote, team, flexible):")
	goals = st.text_input("🎯 Your Career Goals (e.g., high salary, impact, creativity):")
	submitted = st.form_submit_button("✨ Get Career Advice 🏃‍♂️")

# --- Google Sheets Integration ---
def log_to_gsheets(name, strengths, weaknesses, interests, work_style, goals):
	try:
		scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
		creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
		client = gspread.authorize(creds)
		sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1CQSDaaG9IFiAd0vChBWTL3rtPJGEr1v2YerQm79Xdh4/edit?gid=0#gid=0").sheet1
		sheet.append_row([name, strengths, weaknesses, interests, work_style, goals])
		return True, "Logged successfully"
	except Exception as e:
		return False, str(e)
st.markdown('</div>', unsafe_allow_html=True)

if submitted:
	# Log to Google Sheets
	success, msg = log_to_gsheets(name, strengths, weaknesses, interests, work_style, goals)
	if success:
		st.success("Your details have been saved to our career backend!")
	else:
		st.warning(f"Google Sheets logging failed: {msg}")

	# Expanded rule-based recommendations (same as before)
	options = []
	plan = {}
	s = strengths.lower()
	i = interests.lower()
	w = work_style.lower()
	g = goals.lower()
    
    
    
	if "coding" in s or "data" in i or "ai" in i or "blockchain" in i or "web3" in i:
		options += ["AI Engineer", "Blockchain Developer", "Product Designer (UX/UI)", "Tech Startup Founder"]
		plan["AI Engineer"] = {
			"Skills": ["Python", "Machine Learning", "Prompt Engineering", "Deep Learning"],
			"Courses": ["DeepLearning.AI", "fast.ai", "Stanford CS224n"],
			"Next Steps": ["Build AI apps", "Experiment with LLMs", "Join AI hackathons"]
		}
		plan["Blockchain Developer"] = {
			"Skills": ["Solidity", "Smart Contracts", "Web3.js", "Security"],
			"Courses": ["CryptoZombies", "Buildspace", "Coursera Blockchain"],
			"Next Steps": ["Create dApps", "Contribute to open source", "Network in Web3"]
		}
		plan["Product Designer (UX/UI)"] = {
			"Skills": ["Figma", "User Research", "Prototyping", "Design Thinking"],
			"Courses": ["Figma Crash Course", "Coursera UI/UX", "Google UX Certificate"],
			"Next Steps": ["Design for startups", "Build a portfolio", "Freelance gigs"]
		}
		plan["Tech Startup Founder"] = {
			"Skills": ["Pitching", "Growth Hacking", "Leadership", "Product Management"],
			"Courses": ["Y Combinator Startup School", "Udemy Growth Hacking", "LinkedIn Learning"],
			"Next Steps": ["Launch MVP", "Find co-founders", "Pitch to VCs"]
		}
	if "art" in i or "creative" in s or "content" in i or "video" in i or "social" in i:
		options += ["Content Creator", "Digital Marketer", "NFT Artist", "Influencer"]
		plan["Content Creator"] = {
			"Skills": ["Video Editing", "Storytelling", "Social Media", "Branding"],
			"Courses": ["YouTube Creator Academy", "Skillshare", "Udemy"],
			"Next Steps": ["Start a channel", "Grow your audience", "Monetize your content"]
		}
		plan["Digital Marketer"] = {
			"Skills": ["SEO", "Analytics", "Copywriting", "Growth Hacking"],
			"Courses": ["Google Digital Garage", "HubSpot Academy", "Coursera Marketing"],
			"Next Steps": ["Run ad campaigns", "Build a portfolio", "Work with brands"]
		}
		plan["NFT Artist"] = {
			"Skills": ["Digital Art", "NFT Minting", "Community Building"],
			"Courses": ["NFT School", "OpenSea Tutorials", "Skillshare"],
			"Next Steps": ["Create NFT collections", "Sell on OpenSea", "Engage with collectors"]
		}
		plan["Influencer"] = {
			"Skills": ["Personal Branding", "Content Strategy", "Networking"],
			"Courses": ["Influencer Masterclass", "Skillshare", "LinkedIn Learning"],
			"Next Steps": ["Collaborate with brands", "Grow your following", "Host live events"]
		}
	if "leadership" in i or "team" in w or "impact" in g or "sustainability" in i or "climate" in i:
		options += ["Sustainability Consultant", "Community Manager", "Startup Founder", "Product Manager"]
		plan["Sustainability Consultant"] = {
			"Skills": ["ESG", "Data Analysis", "Communication", "Green Tech"],
			"Courses": ["Coursera Sustainability", "edX Climate Change", "LinkedIn Learning"],
			"Next Steps": ["Work on green projects", "Network in climate tech", "Get certified"]
		}
		plan["Community Manager"] = {
			"Skills": ["Engagement", "Event Planning", "Social Media", "Leadership"],
			"Courses": ["Community Management Masterclass", "LinkedIn Learning", "Udemy"],
			"Next Steps": ["Host online events", "Grow communities", "Collaborate with brands"]
		}
		plan["Startup Founder"] = {
			"Skills": ["Pitching", "Growth Hacking", "Leadership", "Product Management"],
			"Courses": ["Y Combinator Startup School", "Udemy Growth Hacking", "LinkedIn Learning"],
			"Next Steps": ["Launch MVP", "Find co-founders", "Pitch to VCs"]
		}
		plan["Product Manager"] = {
			"Skills": ["Agile", "Scrum", "Product Strategy", "User Research"],
			"Courses": ["Coursera Product Management", "PMI Certification", "LinkedIn Learning"],
			"Next Steps": ["Lead product teams", "Build product roadmaps", "Apply for PM roles"]
		}
	if not options:
		options = ["AI Engineer", "Content Creator", "Sustainability Consultant", "Product Designer (UX/UI)"]
		plan["AI Engineer"] = {
			"Skills": ["Python", "Machine Learning", "Prompt Engineering", "Deep Learning"],
			"Courses": ["DeepLearning.AI", "fast.ai", "Stanford CS224n"],
			"Next Steps": ["Build AI apps", "Experiment with LLMs", "Join AI hackathons"]
		}
		plan["Content Creator"] = {
			"Skills": ["Video Editing", "Storytelling", "Social Media", "Branding"],
			"Courses": ["YouTube Creator Academy", "Skillshare", "Udemy"],
			"Next Steps": ["Start a channel", "Grow your audience", "Monetize your content"]
		}
		plan["Sustainability Consultant"] = {
			"Skills": ["ESG", "Data Analysis", "Communication", "Green Tech"],
			"Courses": ["Coursera Sustainability", "edX Climate Change", "LinkedIn Learning"],
			"Next Steps": ["Work on green projects", "Network in climate tech", "Get certified"]
		}
		plan["Product Designer (UX/UI)"] = {
			"Skills": ["Figma", "User Research", "Prototyping", "Design Thinking"],
			"Courses": ["Figma Crash Course", "Coursera UI/UX", "Google UX Certificate"],
			"Next Steps": ["Design for startups", "Build a portfolio", "Freelance gigs"]
		}

	st.success(f"Hi {name}, based on your inputs, here are some recommended career paths:")
	for career in options:
		st.markdown(f"### {career}")
		st.markdown(f"**Key Skills:** {', '.join(plan[career]['Skills'])}")
		st.markdown(f"**Recommended Courses:** {', '.join(plan[career]['Courses'])}")
		st.markdown(f"**Next Steps:** {', '.join(plan[career]['Next Steps'])}")

# --- LangChain UI for LLM-powered advice ---

# Chatbot removed
