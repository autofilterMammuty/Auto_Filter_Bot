class script(object):

    # ─────────────────────────────────────────────────────────────
    # 👋 START / WELCOME
    # ─────────────────────────────────────────────────────────────

    START_TXT = """<b>👋 Hey {},</b>

<b>🤖 I am <a href="https://t.me/{}">{}</a> — your powerful Auto Filter Bot.</b>

✨ <b>Fast Search</b> • 🎬 <b>Movies & Series</b> • ⚡ <b>Premium Features</b>

<blockquote>🔎 Search for your favorite movies or series and get results instantly.</blockquote>

💎 <b>Powered & Customized by <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    GSTART_TXT = """<b>👋 Hey {},</b>

<b>🤖 I am <a href="https://t.me/{}">{}</a> — your powerful Auto Filter Bot.</b>

🎬 Search • ⚡ Filter • 💎 Premium

<blockquote>🔎 Find your favorite movies and series with a simple search.</blockquote>

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # 🆘 HELP
    # ─────────────────────────────────────────────────────────────

    HELP_TXT = """<b>🆘 HOW TO REQUEST MOVIES & SERIES</b>

<blockquote>Follow these simple steps to get the best search results.</blockquote>

<b>1️⃣ Find the correct title</b>
Search the exact movie or series name on Google.

<b>2️⃣ Send the title</b>
Send the name in the group where the bot is active.

<b>3️⃣ Use the correct format</b>

🎬 <b>Movies</b>
➤ <code>Jawan 2023</code>

📺 <b>Series</b>
➤ <code>Loki S01</code>
➤ <code>Loki S01E04</code>

🌐 <b>Language-specific search</b>
➤ <code>Movie Name Hindi</code>
➤ <code>Movie Name Malayalam</code>

⚡ <b>Tip:</b> Use the official spelling and include the year or season when possible.

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # ℹ️ ABOUT
    # ─────────────────────────────────────────────────────────────

    ABOUT_TXT = """<b>╭━━━〔 🤖 BOT DETAILS 〕━━━╮
┃
┃ 👤 <b>Bot Name</b> : <a href="https://t.me/{}">{}</a>
┃ 👨‍💻 <b>Developer</b> : <a href="{}">Owner</a>
┃ 🐍 <b>Language</b> : <a href="https://www.python.org/">Python 3</a>
┃ 📚 <b>Library</b> : <a href="https://docs.pyrogram.org/">Pyrogram</a>
┃ 🗄️ <b>Database</b> : <a href="https://www.mongodb.com/">MongoDB</a>
┃ ☁️ <b>Hosting</b> : Heroku
┃ 🛠️ <b>Build</b> : v1.4 [ Stable ]
┃
┃ 💎 <b>Credits</b> :
┃ <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a>
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯</b>"""

    # ─────────────────────────────────────────────────────────────
    # 🔄 RESTART
    # ─────────────────────────────────────────────────────────────

    RESTART_TXT = """<b>♻️ {} BOT RESTARTED</b>

📅 <b>Date</b>     : <code>{}</code>
⏰ <b>Time</b>     : <code>{}</code>
🌐 <b>Timezone</b> : <code>Asia/Kolkata</code>
🛠️ <b>Build</b>    : <code>v1.4 [ Stable ]</code>

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # 📊 STATUS
    # ─────────────────────────────────────────────────────────────

    MULTI_STATUS_TXT = """<b>📊 SYSTEM STATUS</b>

<blockquote>👥 <b>USER DATABASE</b></blockquote>

👤 Total Users   : <code>{0}</code>
👥 Total Groups  : <code>{1}</code>
💎 Premium Users : <code>{2}</code>

<blockquote>🗄️ <b>DATABASE 1</b></blockquote>

📁 Total Files    : <code>{3}</code>
💾 DB Storage     : <code>{4}</code>
☁️ Cluster Usage  : <code>{5}</code> / 512 MB
🟢 Free Storage   : <code>{6}</code>

<blockquote>🗄️ <b>DATABASE 2</b></blockquote>

📁 Total Files    : <code>{7}</code>
💾 DB Storage     : <code>{8}</code>
☁️ Cluster Usage  : <code>{9}</code> / 512 MB
🟢 Free Storage   : <code>{10}</code>

<blockquote>🤖 <b>BOT RESOURCES</b></blockquote>

⏱️ Uptime      : <code>{11}</code>
🧠 RAM Usage   : <code>{12}%</code>
⚙️ CPU Usage   : <code>{13}%</code>
📦 Total Files : <code>{14}</code>

💎 <b>@iqbaleditzzz</b>"""

    STATUS_TXT = """<b>📊 SYSTEM STATUS</b>

<blockquote>👥 <b>USER DATABASE</b></blockquote>

👤 Total Users   : <code>{0}</code>
👥 Total Groups  : <code>{1}</code>
💎 Premium Users : <code>{2}</code>

<blockquote>🗄️ <b>FILE DATABASE</b></blockquote>

📁 Total Files   : <code>{3}</code>
💾 DB Storage    : <code>{4}</code>
☁️ Cluster Usage : <code>{5}</code> / 512 MB
🟢 Free Storage  : <code>{6}</code>

<blockquote>🤖 <b>BOT RESOURCES</b></blockquote>

⏱️ Uptime    : <code>{7}</code>
🧠 RAM Usage : <code>{8}%</code>
⚙️ CPU Usage : <code>{9}%</code>

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # 📝 LOGS / ALERTS
    # ─────────────────────────────────────────────────────────────

    LOG_TEXT_G = """🆕 <b>NEW GROUP</b>

👥 <b>Group</b> : {}
🆔 <b>ID</b> : <code>{}</code>
👤 <b>Members</b> : <code>{}</code>
➕ <b>Added By</b> : {}"""

    LOG_TEXT_P = """🆕 <b>NEW USER</b>

🆔 <b>ID</b> : <code>{}</code>
👤 <b>Name</b> : {}"""

    NT_ADMIN_ALRT_TXT = """🚫 <b>You are not an administrator in this group.</b>"""

    NT_ALRT_TXT = """🚫 <b>This request does not belong to you.</b>"""

    ALRT_TXT = """<b>👋 Hello {},</b>

🚫 <b>This is not your movie request.</b>

📌 Please submit your own request."""

    OLD_ALRT_TXT = """<b>⚠️ Hey {},</b>

You are using an old request message.

🔄 Please send the request again."""

    # ─────────────────────────────────────────────────────────────
    # 💎 PREMIUM
    # ─────────────────────────────────────────────────────────────

    PRE_STREAM = """<b>🔒 PREMIUM FEATURE</b>

💎 This feature is available only for <b>Premium Users</b>.

✨ Unlock:
• 🚀 Faster access
• 🎬 Premium content
• ⚡ Exclusive features

💳 <b>Upgrade to Premium to continue.</b>"""

    PRE_STREAM_ALERT = """<b>⚠️ PREMIUM CONTENT</b>

🔒 This content requires an active Premium subscription.

💎 <b>Upgrade to Premium to unlock it.</b>"""

    # ─────────────────────────────────────────────────────────────
    # 🔎 SEARCH / NOT FOUND
    # ─────────────────────────────────────────────────────────────

    CUDNT = SPELLING_ERROR_TXT = """<b>❌ No exact match found.</b>

😊 <b>Don't worry — choose the correct title below.</b>

<blockquote>🔎 Check the spelling and select the closest matching movie or series.</blockquote>"""

    DEL_MSG = """<b>⚠️ FILE EXPIRATION NOTICE</b>

This movie file/video will be deleted in <b><u><code>{}</code></u></b>.

<blockquote expandable>📌 Please forward the file to another chat or save it before the timer expires.</blockquote>"""

    I_CUDNT = """<b>❌ Sorry, no files were found for your request {}.</b>

🔎 Check the spelling and try again.

<blockquote>
🎬 <b>Movie</b>
➤ <code>Jawan</code>
➤ <code>Jawan 2023</code>

📺 <b>Series</b>
➤ <code>Loki S01</code>
➤ <code>Loki S01E04</code>
➤ <code>Lucifer S03E24</code>

🚫 Avoid special characters such as:
<code>: ( ! , . / ) &lt; &gt;</code>
</blockquote>"""

    MVE_NT_FND = NOT_FOUND_TXT = """<b>😕 MOVIE NOT FOUND</b>

This movie is currently not available in my database.

<blockquote>🔎 Try another spelling, add the release year, or search for a different title.</blockquote>"""

    ALREADY_AVAILABLE_TXT = """<b>👋 Hey {},</b>

✅ <b>Your request is already available!</b>

<blockquote>
📂 <b>Files Found</b> : {}
🔍 <b>Search</b> : <code>{}</code>
</blockquote>

⚠️ This is a <b>support group</b>, so files cannot be sent directly from here.

🔎 <b>Use the search button below.</b>"""

    SEARCHING_TXT = """<b>🔎 Searching for:</b>

<code>{}</code>

⏳ <i>Please wait...</i>"""

    TOP_ALRT_MSG = """🔎 <b>Searching the database...</b>"""

    # ─────────────────────────────────────────────────────────────
    # 🛠️ MAINTENANCE
    # ─────────────────────────────────────────────────────────────

    MAINTENANCE_TXT = """<b>🛑 SERVICE UNDER MAINTENANCE</b>

Hey {}, our system is currently being updated.

🔧 Some features may be temporarily unavailable.

<blockquote>⏳ Please try again later.</blockquote>

📌 Alternative bot: <b>@MM_MuviBoT</b>"""

    PM_SEARCH_DISABLED_TXT = """<b>🔒 SEARCH IS DISABLED IN PRIVATE CHAT</b>

👋 Hey {},

Movie searches are available only in our movie group.

<blockquote>👉 Join the movie group using the <b>Request Here</b> button below and search for your favorite movie or series there.</blockquote>

🎬 <b>Group Search Only</b>"""

    PM_LOG_TXT = """<b>📩 PRIVATE MESSAGE</b>

👤 <b>Name</b> : {}
🆔 <b>ID</b> : <code>{}</code>
💬 <b>Message</b> : {}"""

    LINK_EXPIRED_TXT = """<b>⏰ LINK EXPIRED</b>

‼️ This link has expired.

🔄 <b>Please try again to generate a new link.</b>"""

    # ─────────────────────────────────────────────────────────────
    # 🎁 REFERRAL
    # ─────────────────────────────────────────────────────────────

    REFER_TXT = """<b>🎁 YOUR REFERRAL LINK</b>

<code>https://t.me/{}?start=reff_{}</code>

<blockquote>
👥 Share your referral link with friends.

🎯 <b>Reward:</b> 10 referral points per successful referral.

💎 <b>100 points = 1 month Premium.</b>
</blockquote>

🚀 Start sharing and earn Premium!"""

    REFER_SELF_ALRT = """<b>😂 NICE TRY!</b>

You cannot use your own referral link.

<blockquote>👥 Share it with your friends and earn referral points instead.</blockquote>"""

    REFER_ALREADY_ALRT = """<b>⚠️ ALREADY INVITED</b>

This user has already been invited."""

    REFER_ALREADY_JOINED_ALRT = """<b>⚠️ ALREADY JOINED</b>

This user has already been invited or joined."""

    REFER_CONGRATS_ALRT = """<b>🎉 REFERRAL REWARD</b>

You earned <b>10 referral points</b> because your invitation was successful.

👤 Invited user: {}"""

    REFER_INVITED_ALRT = """<b>🎉 SUCCESSFULLY INVITED</b>

You have been invited by <b>{}</b>!"""

    # ─────────────────────────────────────────────────────────────
    # 📢 FORCE SUB
    # ─────────────────────────────────────────────────────────────

    FORCESUB_TXT = """<b>👋 Hello {}</b>

🔒 <b>JOIN REQUIRED CHANNELS</b>

You must join all required channels before continuing.

<blockquote>👉 Join every channel listed below, then tap <b>Try Again</b>.</blockquote>"""

    BOT_ADD_TXT = """<b>🎉 THANK YOU FOR ADDING ME!</b>

You added me to <b>{}</b>.

<blockquote>🤝 Need help? Contact our support team for assistance.</blockquote>

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    CHAT_RESTRICTED_TXT = """<b>🚫 CHAT ACCESS RESTRICTED</b>

<blockquote>My administrators have restricted me from working in this chat.

📩 Contact support if you need more information.</blockquote>"""

    LEAVE_CHAT_TXT = """<b>👋 GOODBYE, EVERYONE</b>

<blockquote>My administrator asked me to leave this group, so I have to go.

🔄 If you want to add me again, please contact support.</blockquote>"""

    # ─────────────────────────────────────────────────────────────
    # 🏠 WELCOME
    # ─────────────────────────────────────────────────────────────

    MELCOW_ENG = """<b>👋 Hey {},</b>

🍿 <b>Welcome to {}!</b>

🔎 Search for your favorite <b>movies & series</b> by simply typing the title.

⚡ <b>Fast • Simple • Powerful</b>

<blockquote>💡 Having trouble with a download or search?
📩 Send us a message for support.</blockquote>

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # ⚖️ DISCLAIMER
    # ─────────────────────────────────────────────────────────────

    DISCLAIMER_TXT = """<b>⚖️ DISCLAIMER</b>

This is an open-source project.

The bot indexes files that may already be available on Telegram or elsewhere online. The bot does not claim ownership of third-party content.

<blockquote>📌 Users are responsible for ensuring that their use of any content complies with applicable copyright laws and the terms of the relevant copyright holder.</blockquote>

📩 If you are a copyright owner and believe content is being indexed without authorization, please contact the relevant channel or administrator for removal.

💎 <b>Project Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # 💰 DONATION
    # ─────────────────────────────────────────────────────────────

    DREAMXBOTZ_DONATION = DONATE_TXT = """<b>👋 Hey {},</b>

<blockquote>💖 <b>SUPPORT THE DEVELOPER</b></blockquote>

🔧 Your support helps keep the bot online, maintain servers, fix issues, and develop new features.

💸 <b>Any amount is appreciated.</b>

<blockquote>👇 <b>Choose your donation method</b></blockquote>

📷 QR Code → <a href="{}">Scan Here</a>
💳 UPI ID → <code>{}</code>

‼️ <b>Please send a payment screenshot after donating.</b>

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # 🔎 NO RESULTS
    # ─────────────────────────────────────────────────────────────

    NORSLTS = """<b>🔎 NO RESULTS</b>

🆔 <b>ID</b> : <code>{}</code>
👤 <b>Name</b> : {}

💬 <b>Message</b> : {}"""

    # ─────────────────────────────────────────────────────────────
    # 📦 FILE CAPTION
    # ─────────────────────────────────────────────────────────────

    CAPTION = """<b>🎬 <a href="https://t.me/dreamxbotz">{file_name}</a></b>

━━━━━━━━━━━━━━━━━━
⚡ <b>Powered by <a href="https://t.me/dreamxbotz">DreamXBotz</a></b>
💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>
━━━━━━━━━━━━━━━━━━"""

    # ─────────────────────────────────────────────────────────────
    # 🎬 MOVIE UPDATE
    # ─────────────────────────────────────────────────────────────

    MOVIE_UPDATE_NOTIFY_TXT = """<a href="{poster_url}">📥</a> <a href="{imdb_url}"><b>🔥 NEW {tag} ADDED</b></a>

<blockquote>
<b>🎬 {filename} {year}</b>

┌ 🎭 <b>Genre</b>    : {genres}
├ 📺 <b>OTT</b>      : {ott}
├ 🎞️ <b>Quality</b>  : {quality}
├ 🎧 <b>Audio</b>    : {language}
├ ⭐ <b>Rating</b>   : {rating}
{episodes}
└ 💫 <b>Enjoy & Download</b>
</blockquote>

🔍 <b>SEARCH MOVIE</b> ➜ {search_link}

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # 🎞️ IMDB
    # ─────────────────────────────────────────────────────────────

    IMDB_TEMPLATE_TXT = """<b>🎬 <a href="{url}">{title}</a> (<a href="{url}/releaseinfo">{year}</a>)</b>

⭐ <b>Rating</b> : <a href="{url}/ratings">{rating}</a>
🎭 <b>Genre</b>  : {genres}
🎧 <b>Audio</b>  : {languages}

⏱️ <b>Shown in</b> : {remaining_seconds} <i>sec</i>

👤 <b>Requested by</b> : {message.from_user.mention}"""

    # ─────────────────────────────────────────────────────────────
    # 🖥️ LOGO
    # ─────────────────────────────────────────────────────────────

    LOGO = r"""
██████╗ ██╗██████╗ ███████╗ █████╗ ███╗   ███╗██╗  ██╗██████╗  ██████╗ ████████╗███████╗
██╔══██╗██║██╔══██╗██╔════╝██╔══██╗████╗ ████║╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
██████╔╝██║██████╔╝█████╗  ███████║██╔████╔██║ ╚███╔╝ ██████╔╝██║  ██║   ██║      ███╔═╝
██╔══██╗██║██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║ ██╔██╗ ██╔══██╗██║  ██║   ██║     ██╔══╝
██████╔╝██║██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██╔╝ ██╗██████╔╝╚█████╔╝   ██║    ███████╗
╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝  ╚════╝    ╚═╝    ╚══════╝

BOT WORKING PROPERLY...
CREDITS: @iqbaleditzzz
"""

    # ─────────────────────────────────────────────────────────────
    # 💎 PREMIUM PLANS
    # ─────────────────────────────────────────────────────────────

    PREMIUM_TEXT = """<blockquote>💎 <b>AVAILABLE PREMIUM PLANS</b></blockquote>

┌────────────────────
├ 🗓️ <b>07 Days</b>  — ₹10 / 10 ⭐
├ 🗓️ <b>15 Days</b>  — ₹20 / 20 ⭐
├ 🗓️ <b>30 Days</b>  — ₹40 / 40 ⭐
├ 🗓️ <b>45 Days</b>  — ₹55 / 55 ⭐
└ 🗓️ <b>60 Days</b>  — ₹75 / 75 ⭐

━━━━━━━━━━━━━━━━━━

🏷️ <b>SUBSCRIPTION PROOF</b>
<a href="https://t.me/dreamxbotz">📸 View Proofs</a>

⚠️ Send a payment screenshot after payment.
⏳ After sending the screenshot, please allow some time for activation.

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    PREMIUM_STAR_TEXT = """<b><blockquote>⭐ PAYMENT METHOD: TELEGRAM STARS</blockquote>

💎 You can purchase Premium using Telegram Stars.

1️⃣ Select your preferred plan.
2️⃣ Complete the Stars payment.
3️⃣ Send a screenshot if support requests it.

🆘 For payment issues, contact:
@deendayal_Support_group

🚀 Choose your plan below and enjoy Premium access.</b>"""

    PREMIUM_UPI_TEXT = """<b><blockquote>💳 PAYMENT METHOD: UPI</blockquote>

You can purchase Premium using UPI.

💳 <b>UPI ID</b> : <code>{}</code>

⚠️ Send a payment screenshot after payment.

⏳ Please allow some time for Premium activation.

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b></b>"""

    PREMIUM_END_TEXT = """<b>⚠️ PREMIUM ACCESS EXPIRED</b>

Hey {}, your Premium access has ended.

💎 Thank you for using our service.

📋 Use <code>/plan</code> to view available Premium plans.

<blockquote>🔄 Renew your Premium subscription to continue enjoying exclusive features.</blockquote>"""

    BPREMIUM_TXT = """<blockquote>💎 <b>PREMIUM FEATURES</b></blockquote>

✅ No verification
✅ No unnecessary links
⚡ Direct file access
🚫 Ad-free experience
🚀 High-speed download links
🎥 Streaming links
♾️ Unlimited movie & series searches
🛠️ Priority admin support
⏱️ Faster request processing when available

━━━━━━━━━━━━━━━━━━

🎁 <b>Earn Premium through referrals or purchase a plan.</b>

📋 Check your active plan → <code>/myplan</code>

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    PREPLANS_TXT = PREMIUM_TXT = """<b>👋 Hey {},</b>

<blockquote>💎 <b>PREMIUM PLANS</b></blockquote>

┌────────────────────
├ 🗓️ 07 Days  → ₹10
├ 🗓️ 15 Days  → ₹20
├ 🗓️ 30 Days  → ₹40
├ 🗓️ 45 Days  → ₹55
└ 🗓️ 60 Days  → ₹75

━━━━━━━━━━━━━━━━━━

🏷️ <b>PAYMENT METHODS</b>

💳 UPI ID → <code>{}</code>
📷 QR Code → <a href="{}">Scan Here</a>

🧾 Pay according to your selected plan and enjoy Premium.

⚠️ Send a payment screenshot after payment.
⏳ Allow some time for Premium activation.

💎 Check your plan → <code>/myplan</code>

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b></b>"""

    # ─────────────────────────────────────────────────────────────
    # 💻 SOURCE
    # ─────────────────────────────────────────────────────────────

    SOURCE_TXT = """<b>💻 SOURCE CODE</b>

<blockquote>This is an open-source project. You may use and customize it according to the project's license terms.</blockquote>

🔗 <b>Repository</b> :
<a href="https://github.com/DreamXBotz/Auto_Filter_Bot.git">DreamXBotz Auto Filter Bot</a>

👨‍💻 <b>Credits</b> :
<a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a>"""

    # ─────────────────────────────────────────────────────────────
    # 🔐 VERIFICATION
    # ─────────────────────────────────────────────────────────────

    VERIFICATION_TEXT = """<b>👋 Hey {},</b>

🔐 <b>VERIFICATION REQUIRED</b>

You are not verified today.

Tap <b>Verify</b> to unlock access until the next verification.

📊 <b>Verification:</b> 1/3 ✓

💎 Premium users can access direct files without verification."""

    VERIFY_COMPLETE_TEXT = """<b>👋 Hey {},</b>

✅ <b>1ST VERIFICATION COMPLETED</b>

🎉 You now have unlimited access until the next verification.

💎 Enjoy the service!"""

    SECOND_VERIFICATION_TEXT = """<b>👋 Hey {},</b>

🔐 <b>VERIFICATION REQUIRED</b>

Tap the Verify button to unlock access until the next verification.

📊 <b>Verification:</b> 2/3 ✓

💎 Premium users can access direct files without verification."""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>👋 Hey {},</b>

✅ <b>2ND VERIFICATION COMPLETED</b>

🎉 You now have unlimited access until the next verification."""

    THIRDT_VERIFICATION_TEXT = """<b>👋 Hey {},</b>

🔐 <b>FINAL VERIFICATION</b>

Complete the verification to unlock access for the next full day.

📊 <b>Verification:</b> 3/3 ✓

💎 Premium users can access direct files without verification."""

    THIRDT_VERIFY_COMPLETE_TEXT = """<b>👋 Hey {},</b>

🎉 <b>3RD VERIFICATION COMPLETED</b>

✅ You now have unlimited access for the next full day.

💎 Enjoy the Premium-style experience!"""

    VERIFIED_LOG_TEXT = """<b>✅ USER VERIFIED SUCCESSFULLY</b>

👤 <b>Name</b> : {} [ <code>{}</code> ]
📅 <b>Date</b> : <code>{}</code>

#Verification_{}_Completed"""

    # ─────────────────────────────────────────────────────────────
    # 🛡️ ADMIN COMMANDS
    # ─────────────────────────────────────────────────────────────

    ADMIN_CMD = """<b>🛡️ ADMIN COMMANDS</b>

<blockquote>Powerful controls available to bot administrators.</blockquote>

<b>⚙️ GENERAL</b>
• /start — Start the bot
• /stats — View users and chats
• /restart — Restart the bot
• /maintenance — Toggle maintenance mode

<b>🎬 MOVIE MANAGEMENT</b>
• /del_msg — Manage file deletion notifications
• /movie_update — Toggle movie update notifications
• /delete — Delete a specific file from DB
• /deletefiles — Remove CamRip/PreDVD files
• /send — Send a message to a user

<b>👥 USER & GROUP MANAGEMENT</b>
• /users — List users and IDs
• /chats — List groups and IDs
• /leave — Leave a chat
• /disable — Disable a chat
• /ban — Ban a user
• /unban — Unban a user
• /broadcast — Broadcast to all users
• /grp_broadcast — Broadcast to connected groups

<b>💎 PREMIUM</b>
• /add_premium — Add Premium user
• /remove_premium — Remove Premium user
• /premium_users — List Premium users
• /get_premium — Get Premium user info

<b>🔐 VERIFICATION</b>
• /verify — Toggle group verification
• /logs — View recent errors

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""

    # ─────────────────────────────────────────────────────────────
    # 👥 GROUP COMMANDS
    # ─────────────────────────────────────────────────────────────

    GROUP_CMD = """<b>👥 GROUP COMMANDS</b>

<blockquote>Customize the bot for your group.</blockquote>

<b>⚙️ SETTINGS</b>
• /settings — Open group settings
• /reset_group — Reset group settings
• /details — View current settings

<b>🔗 SHORTENERS</b>
• /set_shortner — Set the 1st shortener
• /set_shortner_2 — Set the 2nd shortener
• /set_shortner_3 — Set the 3rd shortener

<b>🎥 TUTORIALS</b>
• /set_tutorial — Set the 1st tutorial
• /set_tutorial_2 — Set the 2nd tutorial
• /set_tutorial_3 — Set the 3rd tutorial

<b>🔐 VERIFICATION</b>
• /set_time — Set 1st verification gap
• /set_time_2 — Set 2nd verification gap
• /set_log_channel — Set verification log channel

<b>📢 FORCE SUBSCRIPTION</b>
• /set_fsub — Set force-sub channel
• /remove_fsub — Remove force-sub channel

💎 <b>Credits: <a href="https://t.me/iqbaleditzzz">@iqbaleditzzz</a></b>"""
