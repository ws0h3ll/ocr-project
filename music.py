import pafy
import vlc

url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
Inst = vlc.Instance()
player = Inst.media_player_new()
Media = Inst.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
