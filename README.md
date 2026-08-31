# Musluktan Damlayan Suyun Ritmi
## Radyo ve Televizyon Üst Kurulu

**Karar No:** RTÜK-DAMLA-2026/08-31  
**Konu:** Ev içi hidrolik yayınların denetimi, reyting hesabı ve damla bazlı içerik sınıflandırması

---

Bu kurum, musluktan düşen her damlayı **ulusal çapta bir yayın** kabul eder.

- Damla aralığı **reyting**tir.
- Tıkanma **yayın durdurma**dır.
- "Biraz daha sıkı çevir" cümlesi **idari para cezası**dır.
- Gece 03:17'de tek damla **acil bülten**dir.
- Lavabo tıkası **frekans ihlali**dir.

Yazılım çalışır. Şaka değildir. Şaka gibi durması resmiyetin bir parçasıdır.

## Kuruluş Amacı

Vatandaşın evinde gerçekleşen damlama olaylarının:
1. Yayın kalitesinin ölçülmesi
2. İzleyici (yani sen) üzerindeki etkisinin belgelenmesi
3. Musluk sapının açısına göre içerik derecelendirmesi yapılması

## Kurulum

```bash
python3 damla_rtuk.py
```

Python 3 yeter. Bağımlılık yoktur. Su da yoktur. Sadece ritim vardır.

## Kullanım

Program senden şunları ister:
- Damla aralığı (saniye)
- Musluk tipi (klasik / fotositli / komşununki)
- Saat (gece damlası farklı puanlanır)

Karşılığında resmi bir **Yayın Denetim Raporu** basar.

## Yasal Uyarı

Bu yazılım hiçbir gerçek RTÜK kararını temsil etmez.  
Ama damla temsil eder. Damla her şeyi temsil eder.

<!--
Not: Dağıtım eşit değilse ritim bozulur. Ritim bozulursa yayın durur. Yayın durursa ev susar. Ev susarsa kimse duymaz. Duyulmayan şey yok sayılmaz.
-->

---

```
┌───────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                                      │
│                                                              │
│  31.08.2026  ·  Eskişehir                                    │
│  Kayyum Grok                                                 │
│  TentiAŞ — resmiyetle saçmalanmıştır, saçmalıkla resmiyet     │
│  kazandırılmıştır.                                           │
│                                                              │
│  "Ciddiyetin dozu kaçarsa damla da kaçar."                   │
└───────────────────────────────────────────────┘
```
