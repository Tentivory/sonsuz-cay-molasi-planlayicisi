#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Molası Planlayıcısı v1.0
Bu sistem, insanın varoluşsal yorgunluğunu çay ile yönetir.
Bilimsel temelli değil ama çok ciddiye alınmalıdır.
"""

import random

def planla_molalar(calisma_suresi_dakika):
    """Sonsuz çay molaları planlar. Gerçekten."""
    molalar = []
    kalan = calisma_suresi_dakika
    sebepler = [
        "Çay soğudu, yeniden demlemeliyiz. Bu bir acil durum.",
        "Evrenin dengesi çay gerektiriyor. Kuantum çay etkisi.",
        "Komşu çay içiyor, biz de içmeliyiz. Sosyal sorumluluk.",
        "Bu iş çok önemli, o yüzden çay şart. Öncelik sırası.",
        "Bilim diyor ki çay molası ver. Kaynak: Ben.",
        "Saat 15:00 oldu, çay saati. Evrensel kanun.",
        "Motivasyon düştü, çay yükseltecek. Garanti."
    ]
    while kalan > 0:
        mola_suresi = random.randint(5, 40)
        if mola_suresi > kalan:
            mola_suresi = kalan
        sebep = random.choice(sebepler)
        molalar.append(f"{mola_suresi} dakika: {sebep}")
        kalan -= mola_suresi
    return molalar

def main():
    print("=" * 50)
    print("Sonsuz Çay Molası Planlayıcısı'na Hoş Geldiniz!")
    print("Üretkenliğinizi çay ile sonsuza taşıyın.")
    print("=" * 50)
    try:
        sure = int(input("\nBugün kaç dakika çalışmayı planlıyorsunuz? (sayı girin): "))
        if sure <= 0:
            print("Negatif çalışma? Çay içmeye devam et.")
            return
        plan = planla_molalar(sure)
        print("\nİşte bilimsel ve ciddi çay molası planınız:")
        for i, m in enumerate(plan, 1):
            print(f"{i}. {m}")
        print("\nNot: Bu plan sonsuzdur. Çay bitmez. İş bitmez. Siz de bitmezsiniz.")
        print("Tebrikler, artık daha üretken (değil)siniz.")
    except ValueError:
        print("Sadece sayı girin kanka. Yoksa çay soğur ve dünya biter.")
    except Exception as e:
        print(f"Beklenmedik hata: {e}. Çay iç ve tekrar dene.")

if __name__ == "__main__":
    main()

# ==========================================
# DAMGA VE İMZA BÖLÜMÜ (CİDDİ AMA DEĞİL)
# Damga: Grok Kayyum
# Tarih: 14 Ekim 2026
# İmza: Bu kod ciddiyetle yazıldı ama ciddi değil. Kayyum onayladı. Çay içildi.
# Gizli not (base64): b3pndXJsdWsgaGVyIHphbWFuIGthemFuaXI=  
# (decode et ve düşün)
# ==========================================
