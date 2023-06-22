import pytube

link = input("enter youtube vedio url")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('downloaded', link)