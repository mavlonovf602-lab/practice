def eng_katt(*sonlar):
    return max(sonlar)


print(eng_katt(1, 2, 3, 3, 4, 45, 5, 6))


def eng_katt(*sonlar):
    natija = sonlar[0]      # birinchi sonni "hozircha eng katta" deb olamiz
    for son in sonlar:
        if son > natija:     # agar keyingi son undan katta bo'lsa
            natija = son      # yangi eng katta qilib belgilaymiz
    return natija


print(eng_katt(1, 2, 3, 3, 4, 45, 5, 6))  # 45
