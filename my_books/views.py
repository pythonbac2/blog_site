from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def book_list(request):
    html = """
    <h1>Kitoblar ro'yxati</h1>
    <a href="two/"> second page>> </a> <br>
    <a href="pages/O‘tkan kunlar">O‘tkan kunlar>> </a> <br>
    <a href="pages/Turkiston qayg‘usi"> Turkiston qayg‘usi>> </a> <br>
    <a href="pages/Boburnoma "> Boburnoma >> </a> <br>
    <a href="pages/Yulduzli tunlar"> Yulduzli tunlar>> </a> <br>
    <a href="pages/Shum bola"> Shum bola>> </a> 
    
    """
    return HttpResponse(html)


def second_view(request):
    html = """
    <h1>Second page</h1>
    <h2>Ikkinchi bo'lim</h2>

    <a href="../"> firts page </a>
    """
    return HttpResponse(html)


def pages(request, page):
    if page == "O‘tkan kunlar":
        html = f"""
        <h1>Page {page}</h1>
        <p>
        Oʻtkan kunlar, baʼzi manbalarda Oʻtgan kunlar – oʻzbek yozuvchisi Abdulla Qodiriy qalamiga mansub oʻzbek adabiyotidagi ilk roman[1]. 1969-yil „Oʻzbekfilm“ kinostudiyasida ushbu roman asosida „Oʻtgan kunlar“ nomli film suratga olingan. Adib romanni yozishda arab yozuvchisi Jurji Zaydon asarlaridan ilhomlangan[2]. Roman 1920-yillar boshida yozilgan boʻlib, 1922-yil ilk bor „Inqilob“ jurnalida chop etilgan va 1926-yilda alohida kitob holida nashr etilgan[3].
        </p>
        <a href="../"> << first page </a>        
        """
    elif page == "Turkiston qayg‘usi":
        html = f"""
        <h1>Page {page}</h1>
        <p>
        Turkiston qaygʻusi — Alixontoʻra Shokirxontoʻra oʻgʻlining tarixga oid asarlaridan biri hisoblanadi. Asar 1917—1950-yillar mobaynida Gʻarbiy va Sharqiy Turkistonda sodir boʻlgan voqealarni koʻpchilikka maʼlum boʻlmagan tomonlarini ochib beradi. „Turkiston qaygʻusi“ asari 1966—1973-yillarda Toshkentda yoziladi[1]. Asarning birinchi qismi muallifning oʻz qoʻli bilan 1969-yilda yozib bitirilgan. Ikkinchi qismi esa muallif xohishiga koʻra oʻgʻli Asilxon tomonidan 1969-yildan boshlab bir necha yil davomida yozilgan va asar butun holatga keltirilgan[2].
        </p>
        <a href="../"> << first page </a>
        """
    elif page == "Boburnoma":
        html = f"""
        <h1>Page {page}</h1>
        <p>
        Boburnoma — jahon adabiyoti va manbashunosligidagi muhim va noyob yodgorlik; oʻzbek adabiyotida dastlabki nasriy memuar va tarixiy-ilmiy asar. Muallifi Zahiriddin Muhammad Bobur. Eski oʻzbek (chigʻatoy) tilida yozilgan (taxminan 1518/1519—1530). „Boburiya“, „Voqeoti Bobur“, „Voqeanoma“, „Tuzuki Boburiy“, „Tabaqoti Boburiy“, „Tavorixi Boburiy“ kabi nomlar bilan ham maʼlum. Boburning oʻzi esa „Vaqoye“ va „Tarix“ degan nomlarni ishlatgan. Boburnomada 1494—1529-yillarda Markaziy Osiyo, Afgʻoniston va Hindistonda sodir boʻlgan tarixiy-siyosiy voqealar yilma-yil oʻta aniqlik bilan bayon qilingan boʻlib, ular muallif hayoti va siyosiy faoliyati bilan bevosita bogʻliqdir.
        </p>
        <a href="../"> << first page </a>
        """
    elif page == "Yulduzli tunlar":
        html = f"""
        <h1>Page {page}</h1>
        <p>
        „Yulduzli Tunlar“ – oʻzbek yozuvchisi Pirimqul Qodirov qalamiga mansub tarixiy roman. Asarda Zahiriddin Muhammad Bobur hayoti haqida soʻz yuritiladi. Qodirov mazkur roman ustida oʻn yil (1969—1978) davomida ish olib borgan[1]. „Yulduzli tunlar“ga „Boburnoma“ hamda „Humoyunnoma“ asarlari asosiy manba boʻlib xizmat qilgan.
        </p>
        <a href="../"> << first page </a>
        """
    elif page == "Shum bola":
        html = f"""
        <h1>Page {page}</h1>
        <p>
        „Shum bola“ — oʻzbek yozuvchisi va shoiri Gʻafur Gʻulom qalamiga mansub qissa. Muallif asarni 1936-yil yozgan. Qissa bir necha marta nashr qilingan. Qissada ijodkorning bolaligi, XX asr boshidagi Toshkent hayoti tasvirlangan.
        Qissa oʻtkir hajviy asar boʻlib, haqiqiy voqealar va shaxslar taqdiriga asoslangan. Asar markazida yozuvchining hayotidan olingan koʻp faktlar turgan boʻlsa-da, u avtobiografik emas. Unda haqiqiy tarixiy faktlarga nisbatan badiiy toʻqima, fantaziya kuchli.
        </p>
        <a href="../"> << first page </a>
        """
    else:
        html = f"""
        <h1>{page}</h1>
        """

    return HttpResponse(html)