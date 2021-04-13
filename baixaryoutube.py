import pytube

print('<<Naves Youtube Downloader Pro>>')

def tipo():
    
    tipos = input('\n(1)Video or (2)Audio: ')
    
    if tipos == '1':
        video()
    elif tipos == '2':
        audio()
    else:
        tipo() 

def video():
    print('\n======={ Download Video }=======')
    while True:
        link = input("Link do video: ")
        if "https://www.youtube.com/" in link: 
            youtube = pytube.YouTube(link)
            video = youtube.streams.get_highest_resolution()
            author = youtube.author
            #description = video.description

            video.download()
            print(f'Download Concluido: {author}')
        else:
            print('Erro no link')

def audio():
    print("\n======={ Download Audio }=======")
    while True:
        link = input("Link do video: ")
        if "https://www.youtube.com/" in link:
            youtube = pytube.YouTube(link)
            video = youtube.streams.get_audio_only()
            author = youtube.author
            #description = youtube.description

            video.download()
            print(f'Download Concluido: {author}')
        else:
            print('Erro no link')

tipo()