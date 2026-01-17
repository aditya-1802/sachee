import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Sachee ❤️", page_icon="❤️", layout="centered")
html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body {
    margin: 0;
    background: linear-gradient(135deg, #fff1f5, #fde2e8, #f8cdda);
    background-size: 200% 200%;
    animation: softFlow 25s ease infinite;
    overflow-x: hidden;
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
    opacity: 0.4;
    z-index: 1;
}

@keyframes floatUp {
    from { transform: translateY(0); }
    to { transform: translateY(-120vh); }
}

/* Card */
.card {
    background: rgba(255,255,255,0.98);
    padding: 48px;
    border-radius: 32px;
    box-shadow: 0 30px 70px rgba(0,0,0,0.2);
    max-width: 760px;
    margin: 90px auto;
    animation: fadeIn 1.8s ease;
    position: relative;
    z-index: 5;
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
    margin-bottom: 30px;
}

/* Typing text */
#typing {
    font-size: 21px;
    color: #2b2b2b;
    line-height: 2.05;
    text-align: justify;
    white-space: pre-wrap;
}

/* Ending */
.forever {
    margin-top: 30px;
    text-align: right;
    font-size: 23px;
    font-weight: 600;
    color: #e63946;
}

/* 📱 Mobile adjustments */
@media (max-width: 600px) {
    .card {
        margin: 70px 14px;
        padding: 28px;
        border-radius: 26px;
    }

    .title {
        font-size: 30px;
        margin-bottom: 22px;
    }

    #typing {
        font-size: 17px;
        line-height: 1.85;
    }

    .forever {
        font-size: 18px;
    }
}
</style>
</head>

<body>

<!-- Hearts -->
<div class="heart" style="left:10%; font-size:16px; animation-duration:12s;">❤️</div>
<div class="heart" style="left:25%; font-size:20px; animation-duration:14s;">💖</div>
<div class="heart" style="left:45%; font-size:14px; animation-duration:11s;">💗</div>
<div class="heart" style="left:65%; font-size:22px; animation-duration:15s;">💞</div>
<div class="heart" style="left:85%; font-size:18px; animation-duration:13s;">💘</div>

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
        setTimeout(typeWriter, Math.random() * 35 + 20);
    }
}
typeWriter();
</script>

</body>
</html>
"""

