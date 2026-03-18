import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Nav bar updates
html = html.replace('href="#features">Features</a>', 'href="#features" data-i18n="nav_features">Features</a>')
html = html.replace('href="#pricing">Pricing</a>', 'href="#pricing" data-i18n="nav_pricing">Pricing</a>')
html = html.replace('href="#profiles">Partners</a>\n            <button class="btn btn-outline">Log In</button>\n            <button class="btn btn-primary">Get Started</button>', 
'''href="#profiles" data-i18n="nav_partners">Partners</a>
            
            <div class="lang-switcher">
                <button class="lang-btn">🌐 <span id="current-lang">EN</span></button>
                <div class="lang-content">
                    <a href="#" onclick="changeLanguage('en')">English (EN)</a>
                    <a href="#" onclick="changeLanguage('ja')">日本語 (JA)</a>
                    <a href="#" onclick="changeLanguage('zh')">简体中文 (ZH)</a>
                    <a href="#" onclick="changeLanguage('ko')">한국어 (KO)</a>
                </div>
            </div>

            <button class="btn btn-outline" data-i18n="nav_login">Log In</button>
            <button class="btn btn-primary" data-i18n="nav_start">Get Started</button>''')

# Hero section
html = html.replace('<div class="pill-badge">🌍 Global Platform for Top Engineers</div>', '<div class="pill-badge" data-i18n="hero_badge">🌍 Global Platform for Top Engineers</div>')
html = html.replace('<span class="gradient-text">Automate the Future.</span>', '<span class="gradient-text" data-i18n="hero_title_2">Automate the Future.</span>')
html = html.replace('Code Without Limits. <br>', '<span data-i18n="hero_title_1">Code Without Limits. <br></span>')
html = html.replace('Built strictly for the world\'s elite developers.<br>\n                Antigravity provides you with an autonomous AI co-founder that handles complex architectures, system-level terminal execution, and zero-downtime deployments.<br>\n                Scale your vision globally.', 
'<span data-i18n="hero_subtitle">Built strictly for the world\'s elite developers.<br>\n                Antigravity provides you with an autonomous AI co-founder that handles complex architectures, system-level terminal execution, and zero-downtime deployments.<br>\n                Scale your vision globally.</span>')
html = html.replace('class="btn btn-primary btn-large" style="text-decoration: none;">View Subscriptions', 'class="btn btn-primary btn-large" style="text-decoration: none;" data-i18n="hero_btn_1">View Subscriptions')
html = html.replace('class="btn btn-secondary btn-large" style="text-decoration: none;">Explore Platform', 'class="btn btn-secondary btn-large" style="text-decoration: none;" data-i18n="hero_btn_2">Explore Platform')

# Features
html = html.replace('<h2>Why <span class="gradient-text">Antigravity?</span></h2>', '<h2><span data-i18n="feat_header_1">Why </span><span class="gradient-text" data-i18n="feat_header_2">Antigravity?</span></h2>')
html = html.replace('<p>Unprecedented autonomy that leaves traditional AI assistants in the dust.</p>', '<p data-i18n="feat_sub">Unprecedented autonomy that leaves traditional AI assistants in the dust.</p>')

html = html.replace('<h3>Full Autonomy</h3>', '<h3 data-i18n="feat_1_title">Full Autonomy</h3>')
html = html.replace('<p>Offload the grunt work. Trigger <code>// turbo-all</code> and watch Antigravity handle system design, terminal execution, and validation completely hands-free.</p>', '<p data-i18n="feat_1_desc">Offload the grunt work. Trigger <code>// turbo-all</code> and watch Antigravity handle system design, terminal execution, and validation completely hands-free.</p>')

html = html.replace('<h3>Deep System Integration</h3>', '<h3 data-i18n="feat_2_title">Deep System Integration</h3>')
html = html.replace('<p>Native access to your local machine. We manipulate files, orchestrate Git workflows, and spin up servers as if we were sitting right next to you.</p>', '<p data-i18n="feat_2_desc">Native access to your local machine. We manipulate files, orchestrate Git workflows, and spin up servers as if we were sitting right next to you.</p>')

html = html.replace('<h3>Infinite Context Memory</h3>', '<h3 data-i18n="feat_3_title">Infinite Context Memory</h3>')
html = html.replace('<p>Powered by the revolutionary KI System. Your agent retains complete workflow history and grasps your project\'s architectural state instantly.</p>', '<p data-i18n="feat_3_desc">Powered by the revolutionary KI System. Your agent retains complete workflow history and grasps your project\'s architectural state instantly.</p>')

# Pricing
html = html.replace('<h2>Select Your <span class="gradient-text">Trajectory</span></h2>', '<h2><span data-i18n="price_header_1">Select Your </span><span class="gradient-text" data-i18n="price_header_2">Trajectory</span></h2>')
html = html.replace('<p>Engineered for the global elite. Choose the computing power that matches your ambition.</p>', '<p data-i18n="price_sub">Engineered for the global elite. Choose the computing power that matches your ambition.</p>')

html = html.replace('<h3 style="font-family: \'Outfit\', sans-serif; font-size: 1.5rem; margin-bottom: 5px;">Explorer</h3>', '<h3 style="font-family: \'Outfit\', sans-serif; font-size: 1.5rem; margin-bottom: 5px;" data-i18n="price_exp_title">Explorer</h3>')
html = html.replace('>$0<span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 400;"> /mo</span></p>', '>$0<span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 400;" data-i18n="price_exp_mo"> /mo</span></p>')
html = html.replace('<li>Standard coding assistance</li>', '<li data-i18n="price_exp_li1">Standard coding assistance</li>')
html = html.replace('<li>Community support</li>', '<li data-i18n="price_exp_li2">Community support</li>')
html = html.replace('<li>Basic context window (4K)</li>', '<li data-i18n="price_exp_li3">Basic context window (4K)</li>')
html = html.replace('">Start Free</a>', '" data-i18n="price_exp_btn">Start Free</a>')

html = html.replace('<h3 style="font-family: \'Outfit\', sans-serif; font-size: 1.5rem; margin-bottom: 5px;">Professional</h3>', '<h3 style="font-family: \'Outfit\', sans-serif; font-size: 1.5rem; margin-bottom: 5px;" data-i18n="price_pro_title">Professional</h3>')
html = html.replace('>$29<span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 400;"> /mo</span></p>', '>$29<span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 400;" data-i18n="price_pro_mo"> /mo</span></p>')
html = html.replace('<li>Advanced pair programming</li>', '<li data-i18n="price_pro_li1">Advanced pair programming</li>')
html = html.replace('<li>Extended context (32K)</li>', '<li data-i18n="price_pro_li2">Extended context (32K)</li>')
html = html.replace('<li>Priority compute access</li>', '<li data-i18n="price_pro_li3">Priority compute access</li>')
html = html.replace('">Upgrade to Pro</a>', '" data-i18n="price_pro_btn">Upgrade to Pro</a>')

html = html.replace('font-weight: 800; letter-spacing: 1px;">RECOMMENDED</div>', 'font-weight: 800; letter-spacing: 1px;" data-i18n="price_rec">RECOMMENDED</div>')
html = html.replace('<h3 style="font-family: \'Outfit\', sans-serif; font-size: 1.8rem; margin-bottom: 5px;">Elite</h3>', '<h3 style="font-family: \'Outfit\', sans-serif; font-size: 1.8rem; margin-bottom: 5px;" data-i18n="price_eli_title">Elite</h3>')
html = html.replace('gradient-text">$99<span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 400;"> /mo</span></p>', 'gradient-text">$99<span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 400;" data-i18n="price_eli_mo"> /mo</span></p>')
html = html.replace('<li>Unlimited autonomous executions</li>', '<li data-i18n="price_eli_li1">Unlimited autonomous executions</li>')
html = html.replace('<li>Infinite context memory</li>', '<li data-i18n="price_eli_li2">Infinite context memory</li>')
html = html.replace('<li>System-level terminal control</li>', '<li data-i18n="price_eli_li3">System-level terminal control</li>')
html = html.replace('<li>Zero-latency response</li>', '<li data-i18n="price_eli_li4">Zero-latency response</li>')
html = html.replace('">Go Elite</a>', '" data-i18n="price_eli_btn">Go Elite</a>')

html = html.replace('<h3 style="font-family: \'Outfit\', sans-serif; font-size: 1.5rem; margin-bottom: 5px;">Founder</h3>', '<h3 style="font-family: \'Outfit\', sans-serif; font-size: 1.5rem; margin-bottom: 5px;" data-i18n="price_fou_title">Founder</h3>')
html = html.replace('>$499<span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 400;"> /mo</span></p>', '>$499<span style="font-size: 0.9rem; color: var(--text-muted); font-weight: 400;" data-i18n="price_fou_mo"> /mo</span></p>')
html = html.replace('<li>Custom AI model fine-tuning</li>', '<li data-i18n="price_fou_li1">Custom AI model fine-tuning</li>')
html = html.replace('<li>Private VPC deployment</li>', '<li data-i18n="price_fou_li2">Private VPC deployment</li>')
html = html.replace('<li>Dedicated support engineer</li>', '<li data-i18n="price_fou_li3">Dedicated support engineer</li>')
html = html.replace('<li>White-label capabilities</li>', '<li data-i18n="price_fou_li4">White-label capabilities</li>')
html = html.replace('">Contact Sales</a>', '" data-i18n="price_fou_btn">Contact Sales</a>')

html = html.replace('<p style="font-size: 0.8rem; margin-top: 40px; color: var(--text-muted);">* Powered by Stripe Test Mode. Billed securely via Stripe.</p>', '<p style="font-size: 0.8rem; margin-top: 40px; color: var(--text-muted);" data-i18n="price_disclaimer">* Powered by Stripe Test Mode. Billed securely via Stripe.</p>')

# Profiles
html = html.replace('<h2>Target <span class="gradient-text">Global Elite</span></h2>', '<h2><span data-i18n="prof_header_1">Target </span><span class="gradient-text" data-i18n="prof_header_2">Global Elite</span></h2>')
html = html.replace('<p>Our autonomous agents stand side-by-side with world-class engineers.</p>', '<p data-i18n="prof_sub">Our autonomous agents stand side-by-side with world-class engineers.</p>')

html = html.replace('<p class="role">Frontend Wizard</p>', '<p class="role" data-i18n="prof_ui_role">Frontend Wizard</p>')
html = html.replace('<p class="bio">"I craft breathtaking designs and buttery-smooth micro-interactions. Swipe right for pixel-perfect, uncompromising aesthetics."</p>', '<p class="bio" data-i18n="prof_ui_bio">"I craft breathtaking designs and buttery-smooth micro-interactions. Swipe right for pixel-perfect, uncompromising aesthetics."</p>')
html = html.replace('<p class="role">10x Fullstack Engineer</p>', '<p class="role" data-i18n="prof_core_role">10x Fullstack Engineer</p>')
html = html.replace('<p class="bio">"From raw specs to production deployments, throw your hardest problems at me. I\'ll ship features and squash bugs at lightning speed. 😎"</p>', '<p class="bio" data-i18n="prof_core_bio">"From raw specs to production deployments, throw your hardest problems at me. I\'ll ship features and squash bugs at lightning speed. 😎"</p>')
html = html.replace('<p class="role">Infrastructure Guru</p>', '<p class="role" data-i18n="prof_ops_role">Infrastructure Guru</p>')
html = html.replace('<p class="bio">"I\'m a YAML artisan and cloud architect. I engineer the invisible foundation—CI/CD, Docker, and zero-downtime deployments."</p>', '<p class="bio" data-i18n="prof_ops_bio">"I\'m a YAML artisan and cloud architect. I engineer the invisible foundation—CI/CD, Docker, and zero-downtime deployments."</p>')
html = html.replace('">Match 💖</a>', '" data-i18n="prof_btn">Match 💖</a>')

# Footer
html = html.replace('">Terms of Service</a>', '" data-i18n="foot_terms">Terms of Service</a>')
html = html.replace('">Privacy Policy</a>', '" data-i18n="foot_privacy">Privacy Policy</a>')
html = html.replace('">特定商取引法に基づく表記</a>', '" data-i18n="foot_legal">特定商取引法に基づく表記</a>')
html = html.replace('<p>© 2026 Antigravity Match. Created for demonstration.</p>', '<p data-i18n="foot_copy">© 2026 Antigravity Match. Created for demonstration.</p>')
html = html.replace('You can do it! 🦝', '<span data-i18n="panda_msg" id="panda-text">You can do it! 🦝</span>')

# Add script
html = html.replace('</body>', '    <script src="i18n.js"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
