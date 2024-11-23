# 2NHABER Web Sitesi Yük ve Performans Testi Raporu

## Test Amacı
Bu testin amacı, [2NHABER](https://2nhaber.com/) web sitesinin performansını değerlendirmek ve yüksek trafik altında nasıl tepki verdiğini ölçmektir. Yük testi, JMeter aracı kullanılarak gerçekleştirilmiştir.

## Test Yapılandırması

### 1. Test Aracı
- **Apache JMeter**

### 2. Test Türü
- **Yük ve Performans Testi**

### 3. Test Edilen Web Sitesi
- **URL**: [https://2nhaber.com/](https://2nhaber.com/)

### 4. Test Senaryosu
- Ana sayfaya yapılan istekler simüle edilmiştir.
- 40 kullanıcı (Thread) simüle edilmiştir.
- Kullanıcılar 15 saniyelik bir ramp-up süresiyle bağlanmıştır.
- Her kullanıcı, 10 kez ana sayfaya istek göndermektedir.

### 5. Test Planı
- **Thread Group (Kullanıcılar)**:
    - Kullanıcı Sayısı: 40
    - Ramp-Up Süresi: 15 saniye
    - Döngü Sayısı: 10
- **HTTP Request**:
    - Server Name: `2nhaber.com`
    - Path: `/`
    - HTTP Yöntemi: GET
- **Listener (Sonuçlar)**:
    - View Results Tree: Her isteğin sonucunu gösterir.
    - Summary Report: Performans özetini sağlar.

## Test Sonuçları

| İstatistik               | Değer        |
|--------------------------|--------------|
| **Toplam İstek Sayısı**  | 400          |
| **Ortalama Yanıt Süresi (ms)** | 5498     |
| **Min Yanıt Süresi (ms)** | 0            |
| **Max Yanıt Süresi (ms)** | 27229        |
| **Standart Sapma (ms)**   | 4962.97      |
| **Hata Yüzdesi (%)**      | 5%           |

## Yorumlar ve Değerlendirme

- **Toplam İstek Sayısı**: 400 istek başarılı bir şekilde gönderilmiştir. Teste katılan 40 kullanıcı her biri 10 kez işlem yapmıştır.
- **Ortalama Yanıt Süresi**: Ortalama yanıt süresi 5498 ms olarak ölçülmüştür. Bu, kullanıcıların sayfayı yükleme süresi açısından kabul edilebilir bir değerdir. Ancak daha fazla optimizasyon yapılması gerekebilir.
- **Minimum ve Maksimum Yanıt Süresi**: Minimum yanıt süresi 0 ms, maksimum yanıt süresi ise 27229 ms'dir. Maksimum yanıt süresi, sistemin zaman zaman uzun süreli gecikmeler yaşadığını göstermektedir.
- **Standart Sapma**: 4962,97 ms'lik standart sapma, yanıt sürelerinde belirli bir dalgalanma olduğunu göstermektedir. Bu dalgalanmanın nedenlerini anlamak için daha derinlemesine analiz yapılması gereklidir.
- **Hata Yüzdesi**: Test sırasında %5 hata oranı gözlemlenmiştir. Bu oran, web sitesinin genel performansını etkileyebilir ve hata oranını düşürmek için optimizasyon yapılması gerekebilir.

## Sonuçlar ve Öneriler

- **Genel Değerlendirme**: Web sitesi, 40 kullanıcıyla yapılan yük testinde oldukça iyi performans göstermektedir. Ancak, maksimum yanıt süresi yüksek olduğu için, site üzerindeki yük zaman zaman önemli gecikmelere neden olabiliyor.
- **İyileştirme Önerileri**:
    - **Sunucu İyileştirmeleri**: Daha fazla sunucu kaynağı eklenmesi veya mevcut sunucu altyapısının güçlendirilmesi gerekebilir.
    - **Yük Dengeleme**: Trafiğin daha dengeli bir şekilde sunuculara dağıtılması için yük dengeleme teknolojilerinin kullanılması önerilir.
    - **Caching**: Caching mekanizmalarının daha verimli kullanılması ile yanıt sürelerinin iyileştirilmesi sağlanabilir.
    - **Veritabanı Optimizasyonu**: Veritabanı sorgularının optimizasyonu ile yanıt süreleri azaltılabilir.



