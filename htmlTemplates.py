css = """
<style>
.chat-message {
    padding:1.5rem;
    border-radius:0.5rem;
    margin-bottom: 1rem;
    display:flex
}
.chat-message.user{
    background-color: #2b313e
}
.chat-message.bot{
    background-color: #475063
}
.chat-message .avatar {
    width:20%;
}
.chat-message .avatar img{
    max-width: 60px;
    max-height: 60px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message{
    width: 80%;
    padding: 0 1.5rem;
    color: #fff;
}
</style>
"""
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://w7.pngwing.com/pngs/874/871/png-transparent-pop-art-comics-female-comic-book-beauty-avatar-blue-painted-face-thumbnail.png" 
        style="max-height:60px; max-width:60px;border-radius:50%;object-fit:cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://w7.pngwing.com/pngs/487/535/png-transparent-computer-icons-avatar-user-profile-avatar-child-heroes-public-relations-thumbnail.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>

'''