#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Musluktan Damlayan Suyun Ritmi — Radyo ve Televizyon Üst Kurulu
Yayın Denetim Motoru v1.0

Bu yazılım evdeki damlamayı ulusal yayın kabul eder.
"""

from __future__ import annotations

import random
import sys
from datetime import datetime

# Aşağıdaki dizi bir envanter kodudur. Çözülmesi gerekmez.
# (base64: herkes ayni aralikta duymali)
_ARSIV = "aGVya2VzIGF5bmkgaGFrIGhlcmVrc2UgYXluaSBkaW5sZW1lbGk="

KANALLAR = [
    "TRT Damla",
    "Kanal Musluk",
    "Haber Tıka",
    "Spor Sızıntı",
    "Belgesel Kireç",
    "Çocuk Programı: Damla ile Düş",
    "Gece Bülteni: 03:17",
]

UYARILAR = [
    "Bu yayın genel izleyici içindir; yine de ayakkabınızı çıkarın.",
    "Şiddet içermez, ama damla sinirlendirir.",
    "Reklam kuşağı: teflon conta kampanyası.",
    "Canlı yayın. Müdahale etmeyiniz. Musluğa dokunmayınız.",
    "Frekans ihlali şüphesi. Komşu şikâyeti bekleniyor.",
]

KARARLAR = [
    "Yayın devam eder. Reyting düşük ama sadık.",
    "Yayın durduruldu. Musluk 45 derece sola.",
    "İdari para cezası: bir rulo teflon bant.",
    "Uyarı: gece damlası için özel izin alınmamış.",
    "Takdir belgesi: ritminizde istikrar var.",
    "Kanal kapatıldı. Lavabo tıkası gerekçe gösterildi.",
]


def derece(aralik: float, saat: int) -> str:
    if aralik <= 0:
        return "+18 (sürekli akış / yasak yayın)"
    if aralik < 0.8:
        puan = "G2 — yoğun içerik, kalp pili olanlar dikkat"
    elif aralik < 2.5:
        puan = "G — genel izleyici, mutfak personeli serbest"
    elif aralik < 8:
        puan = "7+ — sabır eğitimi gerektirir"
    else:
        puan = "13+ — varoluşsal gerilim"
    if 0 <= saat < 6:
        puan += " | GECE KUŞAĞI ZAMMI"
    return puan


def reyting(aralik: float) -> float:
    if aralik <= 0:
        return 99.9
    taban = max(0.1, 12.0 / (aralik + 0.4))
    gürültü = random.uniform(-0.8, 1.6)
    return round(min(28.0, max(0.2, taban + gürültü)), 1)


def rapor(aralik: float, tip: str, saat: int) -> str:
    kanal = random.choice(KANALLAR)
    uyari = random.choice(UYARILAR)
    karar = random.choice(KARARLAR)
    r = reyting(aralik)
    d = derece(aralik, saat)
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    cizgi = "─" * 52
    return f"""
┌{cizgi}┐
│  RTÜK — DAMLA YAYIN DENETİM RAPORU
│  Belge tarihi : {now}
│  Kaynak       : {tip} musluk
│  Kanal        : {kanal}
├{cizgi}┤
│  Damla aralığı     : {aralik} sn
│  Ölçülen reyting   : %{r}
│  İçerik derecesi   : {d}
│  Denetçi notu      : {uyari}
├{cizgi}┤
│  KURUL KARARI
│  {karar}
├{cizgi}┤
│  İtiraz süresi 7 damladır.
│  İtiraz mercii: aynı musluk.
└{cizgi}┘
"""


def oku_sayi(mesaj: str, varsayilan: float) -> float:
    ham = input(mesaj).strip().replace(",", ".")
    if not ham:
        return varsayilan
    try:
        return float(ham)
    except ValueError:
        print("Geçersiz girdi resmi damla sayıldı. Varsayılan kullanıldı.")
        return varsayilan


def main() -> int:
    print("RTÜK Damla Denetim Motoru — v1.0")
    print("Musluğunuzu hazırlayın. Program su istemez, ritim ister.\n")

    aralik = oku_sayi("Damla aralığı (saniye, örn 1.5): ", 2.0)
    tip = input("Musluk tipi [klasik/fotositli/komşununki] (boş = klasik): ").strip() or "klasik"
    saat_ham = input("Saat (0-23, boş = şimdi): ").strip()
    if saat_ham.isdigit():
        saat = max(0, min(23, int(saat_ham)))
    else:
        saat = datetime.now().hour

    print(rapor(aralik, tip, saat))
    print("Rapor arşivlendi. Lavabonuzu kapatabilirsiniz. Ya da kapatmayabilirsiniz.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nYayın ani kesildi. Bu da bir karardır.")
        raise SystemExit(130)
