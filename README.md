# Baştan Sona Django Projesi

# Proje Raporu - E-Ticaret Uygulaması

## Proje Açıklaması

Bu proje, bir e-ticaret uygulamasının temel yapılarını içeren bir Django projesidir. Proje, kullanıcıların ürünleri listeleyebileceği, satın alabileceği ve yönetebileceği bir platformu simüle eder. Kullanıcılar, ürünleri sepete ekleyebilir, ödeme yapabilir ve siparişlerini görüntüleyebilirler. Proje, sadece yönetici paneli üzerinden ürün eklenmesine ve verilerin JSON formatında sunulmasına odaklanmıştır.

## Kullanılan Teknolojiler ve Araçlar

- Django: Python tabanlı web uygulama çatısı. Django REST framework kullanılarak RESTful API'lar oluşturulmuştur.
- PostgreSQL: Güçlü ve açık kaynaklı veritabanı yönetim sistemi.
- Render: Web uygulamasının yayınlanması ve barındırılması için kullanılan platform.

## Proje Özellikleri

- Kullanıcılar, ürünleri listeleyebilir, detaylarını görüntüleyebilir ve sepete ekleyebilir.
- Kullanıcılar, sepetlerini görüntüleyebilir, ürünleri sepetten çıkarabilir ve ödeme işlemlerini tamamlayabilir.
- Yönetici paneli sayesinde, ürünleri, siparişleri ve kullanıcıları yönetmek mümkündür.
- Sadece yönetici paneli üzerinden ürün eklemesi yapılmaktadır. Kullanıcılar, mevcut ürünleri görüntüleyebilir ve sipariş verebilirler.
- Django REST framework kullanılarak RESTful API'lar oluşturulmuştur, bu sayede harici uygulamalar da verilere erişebilir.
- PostgreSQL veritabanı kullanılarak veriler kalıcı olarak saklanır.
- Render platformu sayesinde web uygulaması yayınlanır ve herkese açık hale gelir.

## Kurulum ve Çalıştırma

1. Projeyi klonlayın:
    
    ```
    git clone <https://github.com/kullaniciadi/etiket.git>
    
    ```
    
2. Proje klasörüne gidin:
    
    ```
    cd etiket
    
    ```
    
3. Sanal ortam oluşturun ve etkinleştirin:
    
    ```
    python -m venv venv
    source venv/bin/activate   # Windows için: venv\\Scripts\\activate
    
    ```
    
4. Gerekli bağımlılıkları yükleyin:
    
    ```
    pip install -r requirements.txt
    
    ```
    
5. Veritabanını oluşturun:
    
    ```
    python manage.py migrate
    
    ```
    
6. Yönetici kullanıcısını oluşturun:
    
    ```
    python manage.py createsuperuser
    
    ```
    
7. Geliştirme sunucusunu başlatın:
    
    ```
    python manage.py runserver
    
    ```
    

## Yönetici Paneli

Yönetici paneline erişmek için aşağıdaki adımları takip edin:

1. Projeyi çalıştırdıktan sonra, web tarayıcınızı açın.
2. URL çubuğuna `http://127.0.0.1:8000/admin/` yazın ve Enter tuşuna basın.
3. Yönetici paneli giriş sayfası açılacaktır. Daha önceden oluşturduğunuz süper kullanıcı adı ve şifrenizi girerek giriş yapın.
4. Yönetici paneline başarıyla giriş yaptıktan sonra, ürünleri ekleyebilir, düzenleyebilir ve silebilirsiniz.

## RESTful API

Proje, RESTful API'lar kullanılarak verilere erişim sağlar. API'ları kullanarak ürün listesini alabilir, ürün detaylarını görüntüleyebilir ve sipariş oluşturabilirsiniz. Aşağıdaki API endpoint'leri kullanılabilir:

- Ürün Listesi: `GET /api/products/`
- Ürün Detayları: `GET /api/products/{product_id}/`
- Sipariş Oluşturma: `POST /api/orders/`

API endpoint'lerini test etmek için, bir API

istemcisi kullanabilir veya `curl` gibi araçları kullanabilirsiniz.

## Sonuç

Bu proje, temel e-ticaret işlevselliğini içeren bir Django uygulamasını ve RESTful API'ları kullanarak verilere erişimi göstermektedir. Aynı zamanda, yönetici paneli aracılığıyla ürünleri yönetmeyi sağlar. Proje, kullanıcıların e-ticaret platformlarının temel özelliklerini nasıl oluşturabileceğini anlamalarına yardımcı olacak bir örnek uygulamadır.

## LİNK
https://djangoappardaemrekarabacak.onrender.com/

https://djangoappardaemrekarabacak.onrender.com/api/products

https://djangoappardaemrekarabacak.onrender.com/admin
