import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Sachee ❤️", page_icon="❤️", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    background: linear-gradient(
        135deg,
        #fff1f5,
        #fde2e8,
        #f8cdda
    );
    background-size: 200% 200%;
    animation: softFlow 25s ease infinite;
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
}

@keyframes softFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating hearts */
.heart {
    position: fixed;
    bottom: -30px;
    animation: floatUp linear infinite;
    opacity: 0.5;
}

@keyframes floatUp {
    from { transform: translateY(0); }
    to { transform: translateY(-110vh); }
}

/* Card */
.card {
    background: rgba(255,255,255,0.98);
    padding: 50px;
    border-radius: 35px;
    box-shadow: 0 40px 80px rgba(0,0,0,0.22);
    max-width: 760px;
    margin: 110px auto;
    animation: fadeIn 2s ease;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #d62828;
    margin-bottom: 35px;
}

/* Typing text */
#typing {
    font-size: 21px;
    color: #2b2b2b;
    line-height: 2.1;
    text-align: justify;
    white-space: pre-wrap;
}

/* Ending */
.forever {
    margin-top: 35px;
    text-align: right;
    font-size: 23px;
    font-weight: 600;
    color: #e63946;
}
</style>

</head>

<body>

<!-- Hearts -->
<div class="heart" style="left:8%; font-size:18px; animation-duration:10s;">❤️</div>
<div class="heart" style="left:18%; font-size:22px; animation-duration:12s;">💖</div>
<div class="heart" style="left:30%; font-size:16px; animation-duration:9s;">💗</div>
<div class="heart" style="left:45%; font-size:26px; animation-duration:14s;">💞</div>
<div class="heart" style="left:60%; font-size:20px; animation-duration:11s;">❤️</div>
<div class="heart" style="left:75%; font-size:24px; animation-duration:13s;">💘</div>
<div class="heart" style="left:88%; font-size:17px; animation-duration:10s;">💓</div>

<div class="card">
    <div class="title">For Sachee ❤️</div>
    <div id="typing"></div>
    <div class="forever">— Forever Yours</div>
</div>

<script>
const text = `Sachee, I don’t know exactly when it happened, but somewhere between ordinary conversations
and quiet moments, you became something permanent in my life.
Not a habit. Not a phase.
A feeling.

You have this way of existing that softens everything around you.
When the world feels loud, you are calm.
When days feel heavy, thinking of you feels like rest.
I don’t love you in loud declarations — I love you in pauses,
in unsent thoughts, in the way my heart reaches for you without asking.

There are parts of me that feel steadier because of you,
and parts that feel braver just knowing you’re there.
Loving you isn’t perfect, but it’s honest.
It’s choosing you in quiet moments,
and meaning it every single time.

You are not something I found —
you are something I keep.`;

let i = 0;
function typeWriter() {
    if (i < text.length) {
        document.getElementById("typing").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, Math.random() * 40 + 20);
    }
}
typeWriter();
</script>

</body>
</html>
"""

components.html(html_code, height=950)
