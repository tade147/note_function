def make_album(singer, album_name):
    """存储歌手及专辑名"""
    album = {'musician' : singer, 'album' : album_name}
    return album

while True:
    print("\n请输入歌手名字:")
    print("请输入专辑名字：")
    print("你可以输入'退出'来退出程序。")
    musician = input("歌手名字: ")
    if musician == '退出':
        break

    album = input("专辑名称: ")
    if album == '退出':
        break
    ma = make_album(musician, album)
    print(ma)

    
