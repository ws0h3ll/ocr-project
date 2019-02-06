import pafy
import vlc

url = raw_input('Enter video id ')
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Inst = vlc.Instance()
player = Inst.media_player_new()
Media = Inst.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
