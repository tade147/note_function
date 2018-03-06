def make_album(singer, album_name, number= '12'):
    """存储歌手及专辑名"""
    album = {'singer': singer, 'album': album_name, 'number' : number}
    return album

m_album = make_album('黄龄', '痒', )
print(m_album)

    
