#!/usr/bin/env python3
"""Text for the privacy policy and terms of use, in every language the app ships.

The facts here are load-bearing, so they were read off the code rather than
assumed. As of this writing Chesshape:

  * stores game state and a compact purchase-delivery ledger locally through
    shared_preferences, may participate in OS backup/device transfer, and runs
    no developer-operated account or data server;
  * ships Google AdMob (google_mobile_ads) for advertising in the free version;
  * includes Firebase Analytics and Crashlytics libraries, but explicitly
    disables collection for both in native configuration and at startup; game
    events resolve to NoopAnalyticsService, which does nothing;
  * offers one non-consumable Premium product and consumable hint packs through
    Apple App Store / Google Play, which process the payments.

If any of that changes, these pages change with it — that is the whole point of
keeping them in one table instead of eleven hand-edited files.
"""

CONTACT = "mnpekdemir.apps@gmail.com"
PLATFORM = "Android &amp; iOS"
EFFECTIVE = "2026-08-19"

# ---------------------------------------------------------------- English
_EN_PRIVACY_INTRO = """<p>This Privacy Policy explains what information is handled when you play
  <strong>Chesshape</strong> ("the App"), a chess-move painting puzzle game
  published by its independent developer ("we", "us"). The short version:
  <strong>we do not ask for your name, e-mail or any account, and we do not run
  any servers that store your data.</strong> The only data processing happens
  on your device and — for advertising — through Google's
  services described below.</p>"""

_EN_PRIVACY = [
    ("1. Data stored only on your device", """<p>The App saves your game state locally on your device, and nowhere else:</p>
  <ul>
    <li>level progress, stars and best scores;</li>
    <li>settings (sound, music, haptics, language, accessibility options);</li>
    <li>hint balance and daily-puzzle streak.</li>
  </ul>
  <p>This data never leaves your device, is not visible to us, and is deleted
  when you uninstall the App. The App does not read your contacts, photos,
  files, location or any other personal content.</p>"""),
    ("2. Advertising (Google AdMob)", """<p>The free version of the App shows ads served by <strong>Google
  AdMob</strong>. To serve and measure ads, Google may collect and process
  data on your device, including your device's <strong>Advertising ID</strong> and
  general device information (model, OS version, language), approximate
  (IP-based) location, and ad interaction data (impressions, clicks).</p>
  <p>We do not receive or store any of this data ourselves; it is processed by
  Google under its own policies. Learn more at
  <a href="https://policies.google.com/privacy" rel="noopener">Google's Privacy Policy</a>
  and <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">How
  Google uses information from apps</a>.</p>
  <ul>
    <li><strong>Consent (EEA/UK/Switzerland):</strong> where required, a consent dialog (Google User Messaging Platform) is shown before any ad personalization, and you can choose non-personalized ads or manage your choices anytime in the App's <em>Settings → Privacy Options</em>.</li>
    <li><strong>Your controls:</strong> device-level advertising controls are also
    available in Android <em>Settings → Privacy → Ads</em> and iOS
    <em>Settings → Privacy &amp; Security → Tracking</em>.</li>
  </ul>"""),
    ("3. What we do NOT do", """<ul>
    <li>No accounts, sign-ups, or collection of names/e-mail addresses.</li>
    <li>No developer-operated servers or databases holding your data.</li>
    <li>No sale of personal information — we have none to sell.</li>
    <li>No third-party analytics SDKs beyond the advertising described above.</li>
  </ul>"""),
    ("4. Children", """<p>The App is a general-audience puzzle game. We do not knowingly collect
  personal information from children. Where consent frameworks apply, ads are
  requested through Google's certified tools. If you believe a child has
  provided personal information through the App, contact us and we will help
  address it.</p>"""),
    ("5. Your rights", """<p>Depending on where you live (including the EU/EEA under GDPR, the UK,
  California under CCPA/CPRA, and Türkiye under KVKK), you may have rights to
  access, correct or delete personal data. Because we do not hold personal
  data ourselves, such requests usually concern data processed by Google —
  see <a href="https://myadcenter.google.com" rel="noopener">Google My Ad Center</a> and
  the links in Section 2. You can always contact us with any privacy question
  and we will do our best to help.</p>"""),
    ("6. Security &amp; data retention", """<p>Game data lives only in the App's private storage on your device,
  protected by the operating system's application sandbox, and exists only as long as the
  App is installed. We retain nothing after uninstall because we store nothing
  elsewhere.</p>"""),
    ("7. Changes to this policy", """<p>If the App's data practices change (for example, if analytics or online
  features are added), this page will be updated and the effective date
  revised before the change ships. Significant changes will also be noted in
  the App's store listing.</p>"""),
]

_EN_TERMS_INTRO = """<p>These Terms of Use ("Terms") govern your use of the mobile game
  <strong>Chesshape</strong> ("the App"), published by its independent developer
  ("we", "us"). By downloading or playing the App you agree to these Terms.
  If you do not agree, please do not use the App.</p>"""

_EN_TERMS = [
    ("1. License", """<p>We grant you a personal, non-exclusive, non-transferable, revocable
  license to install and play the App on Android or iOS devices that you own or
  control, for your own non-commercial entertainment. All rights not expressly
  granted remain with us.</p>"""),
    ("2. Advertising", """<p>The free version shows third-party advertising (Google AdMob), including
  optional rewarded ads that grant in-game hints. Ad content is provided by ad
  networks, not by us. See our <a href="privacy.html">Privacy Policy</a> for
  details on data used for ads.</p>"""),
    ("3. Fair use", """<p>You agree not to: reverse-engineer, decompile or modify the App except
  where the law expressly permits; use cheats, bots or exploits; interfere
  with the App's advertising mechanisms; or use the App in any unlawful
  way.</p>"""),
    ("4. Intellectual property", """<p>The App — including its code, levels, puzzles, artwork, mascot, name,
  logo, music and sounds — is protected by copyright and other laws and is
  owned by the developer or its licensors. These Terms give you no right to
  use the Chesshape name or assets outside the App.</p>"""),
    ("5. Availability &amp; changes", """<p>We may update, change or discontinue the App (or any feature) at any time.
  Updates may be required for continued play. We
  aim to preserve player progress across updates but cannot guarantee it in
  every technical circumstance.</p>"""),
    ("6. Disclaimer of warranties", """<p>The App is provided <strong>"as is" and "as available"</strong>, without
  warranties of any kind, express or implied, including fitness for a
  particular purpose and uninterrupted or error-free operation.</p>"""),
    ("7. Limitation of liability", """<p>To the maximum extent permitted by applicable law, we shall not be liable
  for any indirect, incidental, special or consequential damages, or loss of
  data or progress, arising from your use of the App. Where liability cannot
  be excluded, it is limited to the fullest extent permitted by applicable law. Nothing in these
  Terms limits rights that consumer law grants you and that cannot be waived.</p>"""),
    ("8. Termination", """<p>These Terms apply for as long as you use the App. We may terminate the
  license if you materially breach these Terms. You can end the agreement at
  any time by uninstalling the App.</p>"""),
    ("9. Governing law", """<p>These Terms are governed by the laws of the Republic of Türkiye, without
  prejudice to mandatory consumer protections of your country of residence.</p>"""),
    ("10. Changes to these Terms", """<p>We may revise these Terms from time to time; the effective date above
  will be updated. Continued use of the App after a change means you accept
  the revised Terms.</p>"""),
]

# ---------------------------------------------------------------- Turkish
_TR_PRIVACY_INTRO = """<p>Bu Gizlilik Politikası, bağımsız geliştiricisi ("biz") tarafından yayımlanan
  satranç hamleleriyle boyama bulmacası <strong>Chesshape</strong> ("Uygulama")
  oynanırken hangi bilgilerin işlendiğini açıklar. Kısaca:
  <strong>adınızı, e-postanızı veya herhangi bir hesap bilgisini istemiyoruz ve
  verilerinizi saklayan hiçbir sunucu işletmiyoruz.</strong> Tüm veri işleme
  cihazınızda ve — reklam için — aşağıda açıklanan Google
  hizmetleri üzerinden gerçekleşir.</p>"""

_TR_PRIVACY = [
    ("1. Yalnızca cihazınızda saklanan veriler", """<p>Uygulama oyun durumunuzu yalnızca cihazınızda saklar, başka hiçbir yerde:</p>
  <ul>
    <li>bölüm ilerlemesi, yıldızlar ve en iyi skorlar;</li>
    <li>ayarlar (ses, müzik, titreşim, dil, erişilebilirlik seçenekleri);</li>
    <li>ipucu bakiyesi ve günlük bulmaca serisi.</li>
  </ul>
  <p>Bu veriler cihazınızdan hiç çıkmaz, bizim tarafımızdan görülemez ve
  Uygulamayı kaldırdığınızda silinir. Uygulama kişilerinizi, fotoğraflarınızı,
  dosyalarınızı, konumunuzu veya başka hiçbir kişisel içeriği okumaz.</p>"""),
    ("2. Reklamlar (Google AdMob)", """<p>Uygulamanın ücretsiz sürümü <strong>Google AdMob</strong> tarafından sunulan
  reklamlar gösterir. Reklamları sunmak ve ölçmek için Google, cihazınızdaki
  şu verileri toplayıp işleyebilir: cihazınızın <strong>Reklam Kimliği</strong> ve
  genel cihaz bilgileri (model, işletim sistemi sürümü, dil), yaklaşık
  (IP tabanlı) konum ve reklam etkileşim verileri (gösterim, tıklama).</p>
  <p>Bu verilerin hiçbirini biz almıyor veya saklamıyoruz; Google kendi
  politikaları kapsamında işler. Ayrıntı için
  <a href="https://policies.google.com/privacy" rel="noopener">Google Gizlilik Politikası</a>
  ve <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Google'ın
  uygulamalardan gelen bilgileri nasıl kullandığı</a> sayfalarına bakın.</p>
  <ul>
    <li><strong>Rıza (AEA/BK/İsviçre):</strong> gerekli olduğu yerlerde, reklam kişiselleştirmesinden önce bir rıza penceresi (Google User Messaging Platform) gösterilir; tercihlerinizi Uygulama içindeki <em>Ayarlar → Gizlilik seçenekleri</em> menüsünden dilediğiniz zaman değiştirebilirsiniz.</li>
    <li><strong>Denetim sizde:</strong> cihaz düzeyindeki reklam denetimlerine Android
    <em>Ayarlar → Gizlilik → Reklamlar</em> ve iOS
    <em>Ayarlar → Gizlilik ve Güvenlik → Takip</em> üzerinden de ulaşabilirsiniz.</li>
  </ul>"""),
    ("3. Yapmadıklarımız", """<ul>
    <li>Hesap, kayıt veya ad/e-posta toplama yok.</li>
    <li>Verilerinizi tutan, geliştiriciye ait sunucu veya veritabanı yok.</li>
    <li>Kişisel veri satışı yok — satacak verimiz yok.</li>
    <li>Yukarıda anlatılan reklamcılık dışında üçüncü taraf analitik SDK'sı yok.</li>
  </ul>"""),
    ("4. Çocuklar", """<p>Uygulama genel izleyici kitlesine yönelik bir bulmaca oyunudur. Bilerek
  çocuklardan kişisel bilgi toplamıyoruz. Rıza çerçevelerinin geçerli olduğu
  yerlerde reklamlar Google'ın sertifikalı araçlarıyla istenir. Bir çocuğun
  Uygulama aracılığıyla kişisel bilgi verdiğini düşünüyorsanız bize yazın,
  çözülmesine yardımcı olalım.</p>"""),
    ("5. Haklarınız", """<p>Yaşadığınız yere bağlı olarak (GDPR kapsamında AB/AEA, Birleşik Krallık,
  CCPA/CPRA kapsamında Kaliforniya ve KVKK kapsamında Türkiye dâhil) kişisel
  verilere erişme, düzeltme veya silme haklarınız olabilir. Kişisel veriyi
  kendimiz tutmadığımız için bu tür talepler genelde Google'ın işlediği
  verilerle ilgilidir — <a href="https://myadcenter.google.com" rel="noopener">Google
  Reklam Merkezim</a> sayfasına ve 2. bölümdeki bağlantılara bakın. Gizlilikle
  ilgili her soruda bize yazabilirsiniz.</p>"""),
    ("6. Güvenlik ve saklama süresi", """<p>Oyun verileri yalnızca cihazınızdaki Uygulamaya ait özel alanda,
  işletim sisteminin uygulama korumalı alanı içinde bulunur ve yalnızca Uygulama
  kurulu olduğu sürece var olur. Başka hiçbir yerde saklamadığımız için
  kaldırma sonrası hiçbir şey elimizde kalmaz.</p>"""),
    ("7. Bu politikadaki değişiklikler", """<p>Uygulamanın veri uygulamaları değişirse (örneğin analitik veya çevrimiçi
  özellikler eklenirse), değişiklik yayına girmeden önce bu sayfa güncellenir
  ve yürürlük tarihi yenilenir. Önemli değişiklikler mağaza sayfasında da
  belirtilir.</p>"""),
]

_TR_TERMS_INTRO = """<p>Bu Kullanım Şartları ("Şartlar"), bağımsız geliştiricisi ("biz")
  tarafından yayımlanan <strong>Chesshape</strong> ("Uygulama") mobil oyununu
  kullanımınızı düzenler. Uygulamayı indirerek veya oynayarak bu Şartları
  kabul etmiş olursunuz. Kabul etmiyorsanız lütfen Uygulamayı kullanmayın.</p>"""

_TR_TERMS = [
    ("1. Lisans", """<p>Size, sahibi veya kullanıcısı olduğunuz Android veya iOS cihazlara Uygulamayı
  kurup kendi ticari olmayan eğlenceniz için oynamanız adına kişisel, münhasır
  olmayan, devredilemez ve geri alınabilir bir lisans veriyoruz. Açıkça
  verilmeyen tüm haklar bizde kalır.</p>"""),
    ("2. Reklamlar", """<p>Ücretsiz sürüm üçüncü taraf reklamları (Google AdMob) gösterir; buna
  oyun içi ipucu kazandıran isteğe bağlı ödüllü reklamlar dâhildir. Reklam
  içeriği bizim tarafımızdan değil reklam ağları tarafından sağlanır.
  Reklamlarda kullanılan veriler için
  <a href="privacy-tr.html">Gizlilik Politikamıza</a> bakın.</p>"""),
    ("3. Dürüst kullanım", """<p>Şunları yapmamayı kabul edersiniz: yasanın açıkça izin verdiği hâller
  dışında Uygulamayı tersine mühendislikle çözmek, kaynak koda dönüştürmek
  veya değiştirmek; hile, bot veya açık kullanmak; Uygulamanın reklam
  mekanizmalarına müdahale etmek; Uygulamayı hukuka aykırı biçimde
  kullanmak.</p>"""),
    ("4. Fikrî mülkiyet", """<p>Uygulama — kodu, bölümleri, bulmacaları, görselleri, maskotu, adı,
  logosu, müziği ve sesleri dâhil — telif hakkı ve diğer yasalarla korunur ve
  geliştiriciye veya lisans verenlerine aittir. Bu Şartlar size Chesshape
  adını veya varlıklarını Uygulama dışında kullanma hakkı vermez.</p>"""),
    ("5. Erişilebilirlik ve değişiklikler", """<p>Uygulamayı (herhangi bir özelliği dâhil) istediğimiz zaman
  güncelleyebilir, değiştirebilir veya durdurabiliriz. Oynamaya devam etmek
  için güncelleme gerekebilir. Oyuncu ilerlemesini güncellemeler boyunca
  korumayı hedefliyoruz ancak her teknik durumda garanti edemeyiz.</p>"""),
    ("6. Garanti reddi", """<p>Uygulama <strong>"olduğu gibi" ve "mevcut hâliyle"</strong> sunulur; belirli
  bir amaca uygunluk ile kesintisiz veya hatasız çalışma dâhil olmak üzere
  açık ya da zımni hiçbir garanti verilmez.</p>"""),
    ("7. Sorumluluğun sınırlandırılması", """<p>Yürürlükteki yasaların izin verdiği azami ölçüde, Uygulamayı
  kullanımınızdan doğan dolaylı, arızi, özel veya sonuç olarak ortaya çıkan
  zararlardan ya da veri veya ilerleme kaybından sorumlu değiliz.
  Sorumluluğun hariç tutulamadığı hâllerde, yürürlükteki hukukun izin verdiği
  azami ölçüde sınırlıdır.
  Bu Şartlardaki hiçbir hüküm, tüketici hukukunun size tanıdığı ve
  vazgeçilemez hakları sınırlamaz.</p>"""),
    ("8. Fesih", """<p>Bu Şartlar Uygulamayı kullandığınız sürece geçerlidir. Şartları esaslı
  şekilde ihlal etmeniz hâlinde lisansı sonlandırabiliriz. Uygulamayı
  kaldırarak sözleşmeyi istediğiniz zaman sona erdirebilirsiniz.</p>"""),
    ("9. Uygulanacak hukuk", """<p>Bu Şartlar, ikamet ettiğiniz ülkenin emredici tüketici korumaları saklı
  kalmak kaydıyla Türkiye Cumhuriyeti hukukuna tabidir.</p>"""),
    ("10. Şartlardaki değişiklikler", """<p>Bu Şartları zaman zaman gözden geçirebiliriz; yukarıdaki yürürlük tarihi
  güncellenir. Değişiklikten sonra Uygulamayı kullanmaya devam etmeniz,
  gözden geçirilmiş Şartları kabul ettiğiniz anlamına gelir.</p>"""),
]


def _lang(code, name, flag, *, privacy_title, terms_title, privacy_summary,
          terms_summary, effective_label, app_label, nav_home, contact_label,
          privacy_contact, terms_contact, privacy_intro, privacy_sections,
          terms_intro, terms_sections):
    return {
        "name": name,
        "flag": flag,
        "effective_label": effective_label,
        "app_label": app_label,
        "nav_home": nav_home,
        "contact_label": contact_label,
        "privacy": {
            "title": privacy_title,
            "summary": privacy_summary,
            "intro": privacy_intro,
            "sections": privacy_sections,
            "contact_line": privacy_contact,
        },
        "terms": {
            "title": terms_title,
            "summary": terms_summary,
            "intro": terms_intro,
            "sections": terms_sections,
            "contact_line": terms_contact,
        },
    }


LANGS = {}

LANGS["en"] = _lang(
    "en", "English", "🇬🇧",
    privacy_title="Privacy Policy", terms_title="Terms of Use",
    privacy_summary="Privacy Policy for the Chesshape mobile game.",
    terms_summary="Terms of Use for the Chesshape mobile game.",
    effective_label="Effective date", app_label="App", nav_home="Home",
    contact_label="Contact",
    privacy_contact="Questions or requests about privacy:",
    terms_contact="Questions about these Terms:",
    privacy_intro=_EN_PRIVACY_INTRO, privacy_sections=_EN_PRIVACY,
    terms_intro=_EN_TERMS_INTRO, terms_sections=_EN_TERMS,
)

LANGS["tr"] = _lang(
    "tr", "Türkçe", "🇹🇷",
    privacy_title="Gizlilik Politikası", terms_title="Kullanım Şartları",
    privacy_summary="Chesshape mobil oyunu için Gizlilik Politikası.",
    terms_summary="Chesshape mobil oyunu için Kullanım Şartları.",
    effective_label="Yürürlük tarihi", app_label="Uygulama", nav_home="Ana sayfa",
    contact_label="İletişim",
    privacy_contact="Gizlilikle ilgili soru veya talepler:",
    terms_contact="Bu Şartlarla ilgili sorular:",
    privacy_intro=_TR_PRIVACY_INTRO, privacy_sections=_TR_PRIVACY,
    terms_intro=_TR_TERMS_INTRO, terms_sections=_TR_TERMS,
)

# ------------------------------------------------------- other languages
# Same eight privacy sections and eleven terms sections as English, in the
# order the App's own language list uses. The section numbering is kept
# identical across languages so a support reply can cite "section 2" and mean
# the same thing to every player.

_DE_PRIVACY = [
    ("1. Nur auf Ihrem Gerät gespeicherte Daten", """<p>Die App speichert Ihren Spielstand ausschließlich lokal auf Ihrem Gerät:</p>
  <ul><li>Levelfortschritt, Sterne und Bestwerte;</li>
  <li>Einstellungen (Ton, Musik, Haptik, Sprache, Barrierefreiheit);</li>
  <li>Tipp-Guthaben und Tagesrätsel-Serie.</li></ul>
  <p>Diese Daten verlassen Ihr Gerät nie, sind für uns nicht einsehbar und werden
  bei der Deinstallation gelöscht. Die App liest weder Kontakte noch Fotos,
  Dateien, Standort oder sonstige persönliche Inhalte.</p>"""),
    ("2. Werbung (Google AdMob)", """<p>Die kostenlose Version zeigt Werbung von <strong>Google AdMob</strong>. Zur
  Auslieferung und Messung von Anzeigen kann Google Daten auf Ihrem Gerät
  verarbeiten: die <strong>Werbe-ID</strong>, allgemeine Geräteinformationen (Modell,
  Betriebssystemversion, Sprache), den ungefähren (IP-basierten) Standort sowie
  Interaktionsdaten (Impressionen, Klicks).</p>
  <p>Wir erhalten und speichern diese Daten nicht; sie werden von Google nach
  dessen eigenen Richtlinien verarbeitet. Mehr dazu in der
  <a href="https://policies.google.com/privacy" rel="noopener">Datenschutzerklärung von Google</a>
  und unter <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Wie
  Google Daten aus Apps verwendet</a>.</p>
  <ul><li><strong>Einwilligung (EWR/UK/Schweiz):</strong> wo erforderlich, erscheint vor
  jeder Personalisierung ein Einwilligungsdialog (Google User Messaging
  Platform); Sie können nicht personalisierte Werbung wählen und Ihre Auswahl
  jederzeit unter <em>Einstellungen → Datenschutzoptionen</em> ändern.</li>
  <li><strong>Ihre Kontrolle:</strong> Gerätebezogene Werbeeinstellungen finden Sie
  außerdem unter Android <em>Einstellungen → Datenschutz → Werbung</em> und iOS
  <em>Einstellungen → Datenschutz &amp; Sicherheit → Tracking</em>.</li></ul>"""),
    ("3. Was wir NICHT tun", """<ul><li>Keine Konten, keine Registrierung, keine Erfassung von Namen oder E-Mail-Adressen.</li>
  <li>Keine vom Entwickler betriebenen Server oder Datenbanken mit Ihren Daten.</li>
  <li>Kein Verkauf personenbezogener Daten — wir haben keine.</li>
  <li>Keine Analyse-SDKs von Dritten über die beschriebene Werbung hinaus.</li></ul>"""),
    ("4. Kinder", """<p>Die App ist ein Rätselspiel für ein allgemeines Publikum. Wir erheben nicht
  wissentlich personenbezogene Daten von Kindern. Wo Einwilligungsrahmen gelten,
  werden Anzeigen über die zertifizierten Werkzeuge von Google angefordert.
  Wenn Sie glauben, dass ein Kind personenbezogene Daten übermittelt hat,
  kontaktieren Sie uns.</p>"""),
    ("5. Ihre Rechte", """<p>Je nach Wohnort (u. a. EU/EWR nach DSGVO, UK, Kalifornien nach CCPA/CPRA,
  Türkei nach KVKK) haben Sie ggf. Rechte auf Auskunft, Berichtigung oder
  Löschung. Da wir selbst keine personenbezogenen Daten vorhalten, betreffen
  solche Anfragen meist von Google verarbeitete Daten — siehe
  <a href="https://myadcenter.google.com" rel="noopener">Google My Ad Center</a> und die
  Links in Abschnitt 2. Sie können uns jederzeit schreiben.</p>"""),
    ("6. Sicherheit &amp; Speicherdauer", """<p>Spieldaten liegen nur im privaten Speicher der App auf Ihrem Gerät,
  geschützt durch die App-Sandbox des Betriebssystems, und existieren nur solange die App
  installiert ist. Nach der Deinstallation behalten wir nichts, weil wir nichts
  anderswo speichern.</p>"""),
    ("7. Änderungen dieser Richtlinie", """<p>Ändern sich die Datenpraktiken der App (etwa durch Analyse- oder
  Online-Funktionen), wird diese Seite vor der Auslieferung aktualisiert und das
  Datum angepasst. Wesentliche Änderungen werden auch im Store-Eintrag genannt.</p>"""),
]

_DE_TERMS = [
    ("1. Lizenz", """<p>Wir gewähren Ihnen eine persönliche, nicht ausschließliche, nicht
  übertragbare und widerrufliche Lizenz, die App auf Android- oder iOS-Geräten, die Sie
  besitzen oder kontrollieren, zu Ihrer nicht kommerziellen Unterhaltung zu
  installieren und zu spielen. Alle nicht ausdrücklich gewährten Rechte
  verbleiben bei uns.</p>"""),
    ("2. Werbung", """<p>Die kostenlose Version zeigt Werbung Dritter (Google AdMob), einschließlich
  optionaler Rewarded Ads, die Tipps gewähren. Die Anzeigeninhalte stammen von
  Werbenetzwerken, nicht von uns. Details zu den verwendeten Daten in unserer
  <a href="privacy-de.html">Datenschutzerklärung</a>.</p>"""),
    ("3. Faire Nutzung", """<p>Sie verpflichten sich, die App nicht zurückzuentwickeln, zu dekompilieren
  oder zu verändern, außer wo das Gesetz es ausdrücklich erlaubt; keine Cheats,
  Bots oder Exploits einzusetzen; die Werbemechanismen nicht zu
  stören; und die App nicht rechtswidrig zu nutzen.</p>"""),
    ("4. Geistiges Eigentum", """<p>Die App — Code, Level, Rätsel, Grafik, Maskottchen, Name, Logo, Musik und
  Klänge — ist urheberrechtlich geschützt und gehört dem Entwickler oder seinen
  Lizenzgebern. Diese Bedingungen geben Ihnen kein Recht, den Namen Chesshape
  oder die Inhalte außerhalb der App zu nutzen.</p>"""),
    ("5. Verfügbarkeit &amp; Änderungen", """<p>Wir können die App (oder einzelne Funktionen) jederzeit aktualisieren,
  ändern oder einstellen. Für weiteres Spielen
  können Updates nötig sein. Wir bemühen uns, den Fortschritt über Updates
  hinweg zu erhalten, können dies aber nicht in jedem Fall garantieren.</p>"""),
    ("6. Gewährleistungsausschluss", """<p>Die App wird <strong>„wie besehen" und „wie verfügbar"</strong> bereitgestellt,
  ohne ausdrückliche oder stillschweigende Gewährleistung, einschließlich
  Eignung für einen bestimmten Zweck oder unterbrechungsfreien Betrieb.</p>"""),
    ("7. Haftungsbeschränkung", """<p>Soweit gesetzlich zulässig, haften wir nicht für indirekte, zufällige,
  besondere oder Folgeschäden oder für den Verlust von Daten oder Fortschritt.
  Soweit die Haftung nicht ausgeschlossen werden kann, ist sie im gesetzlich
  zulässigen Umfang begrenzt. Zwingende Verbraucherrechte bleiben unberührt.</p>"""),
    ("8. Beendigung", """<p>Diese Bedingungen gelten, solange Sie die App nutzen. Bei einem
  wesentlichen Verstoß können wir die Lizenz beenden. Sie können die
  Vereinbarung jederzeit durch Deinstallation beenden.</p>"""),
    ("9. Anwendbares Recht", """<p>Es gilt das Recht der Republik Türkei, unbeschadet zwingender
  Verbraucherschutzvorschriften Ihres Wohnsitzlandes.</p>"""),
    ("10. Änderungen dieser Bedingungen", """<p>Wir können diese Bedingungen von Zeit zu Zeit überarbeiten; das oben
  genannte Datum wird aktualisiert. Die weitere Nutzung nach einer Änderung
  gilt als Zustimmung.</p>"""),
]

LANGS["de"] = _lang(
    "de", "Deutsch", "🇩🇪",
    privacy_title="Datenschutzerklärung", terms_title="Nutzungsbedingungen",
    privacy_summary="Datenschutzerklärung für das Mobilspiel Chesshape.",
    terms_summary="Nutzungsbedingungen für das Mobilspiel Chesshape.",
    effective_label="Gültig ab", app_label="App", nav_home="Startseite",
    contact_label="Kontakt",
    privacy_contact="Fragen oder Anliegen zum Datenschutz:",
    terms_contact="Fragen zu diesen Bedingungen:",
    privacy_intro="""<p>Diese Datenschutzerklärung erläutert, welche Informationen verarbeitet
  werden, wenn Sie <strong>Chesshape</strong> („die App") spielen, ein
  Mal-Rätselspiel mit Schachzügen, herausgegeben von seinem unabhängigen
  Entwickler („wir"). Kurz gesagt: <strong>wir fragen weder Namen noch E-Mail
  oder Konto ab und betreiben keine Server, die Ihre Daten speichern.</strong>
  Verarbeitet wird nur auf Ihrem Gerät und — für Werbung — über die
  unten beschriebenen Google-Dienste.</p>""",
    privacy_sections=_DE_PRIVACY,
    terms_intro="""<p>Diese Nutzungsbedingungen („Bedingungen") regeln Ihre Nutzung des
  Mobilspiels <strong>Chesshape</strong> („die App"), herausgegeben von seinem
  unabhängigen Entwickler („wir"). Mit dem Herunterladen oder Spielen stimmen
  Sie diesen Bedingungen zu. Andernfalls nutzen Sie die App bitte nicht.</p>""",
    terms_sections=_DE_TERMS,
)

_ES_PRIVACY = [
    ("1. Datos almacenados solo en tu dispositivo", """<p>La App guarda tu progreso únicamente en tu dispositivo:</p>
  <ul><li>progreso de niveles, estrellas y mejores puntuaciones;</li>
  <li>ajustes (sonido, música, vibración, idioma, accesibilidad);</li>
  <li>saldo de pistas y racha del puzle diario.</li></ul>
  <p>Estos datos nunca salen de tu dispositivo, no son visibles para nosotros y
  se borran al desinstalar la App. La App no lee tus contactos, fotos, archivos,
  ubicación ni ningún otro contenido personal.</p>"""),
    ("2. Publicidad (Google AdMob)", """<p>La versión gratuita muestra anuncios de <strong>Google AdMob</strong>. Para
  publicar y medir anuncios, Google puede tratar datos de tu dispositivo: el
  <strong>ID de publicidad</strong>, información general del dispositivo (modelo,
  versión del sistema, idioma), ubicación aproximada (por IP) y datos de
  interacción (impresiones, clics).</p>
  <p>Nosotros no recibimos ni almacenamos ninguno de esos datos; los trata
  Google conforme a sus propias políticas. Más información en la
  <a href="https://policies.google.com/privacy" rel="noopener">Política de Privacidad de Google</a>
  y en <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">cómo
  usa Google la información de las apps</a>.</p>
  <ul><li><strong>Consentimiento (EEE/RU/Suiza):</strong> cuando corresponde se muestra un
  diálogo de consentimiento (Google User Messaging Platform) antes de
  personalizar anuncios; puedes elegir anuncios no personalizados y cambiar tus
  elecciones en cualquier momento en <em>Ajustes → Opciones de privacidad</em>.</li>
  <li><strong>Tus controles:</strong> los controles publicitarios del dispositivo también
  están disponibles en Android <em>Ajustes → Privacidad → Anuncios</em> y en iOS
  <em>Ajustes → Privacidad y seguridad → Rastreo</em>.</li></ul>"""),
    ("3. Lo que NO hacemos", """<ul><li>Sin cuentas, registros ni recogida de nombres o correos.</li>
  <li>Sin servidores ni bases de datos del desarrollador con tus datos.</li>
  <li>Sin venta de datos personales: no tenemos ninguno que vender.</li>
  <li>Sin SDK de analítica de terceros más allá de la publicidad descrita.</li></ul>"""),
    ("4. Menores", """<p>La App es un juego de puzles para público general. No recogemos
  conscientemente datos personales de menores. Donde aplican marcos de
  consentimiento, los anuncios se solicitan mediante las herramientas
  certificadas de Google. Si crees que un menor ha facilitado datos personales,
  escríbenos y te ayudaremos.</p>"""),
    ("5. Tus derechos", """<p>Según dónde vivas (UE/EEE con el RGPD, Reino Unido, California con
  CCPA/CPRA, Türkiye con KVKK) puedes tener derechos de acceso, rectificación o
  supresión. Como no conservamos datos personales, esas solicitudes suelen
  referirse a datos tratados por Google — consulta
  <a href="https://myadcenter.google.com" rel="noopener">Mi Centro de Anuncios</a> y los
  enlaces de la sección 2. Puedes escribirnos siempre que quieras.</p>"""),
    ("6. Seguridad y conservación", """<p>Los datos del juego residen solo en el almacenamiento privado de la App en
  tu dispositivo, protegidos por el sandbox del sistema operativo, y existen mientras la App
  esté instalada. No conservamos nada tras la desinstalación porque no guardamos
  nada en otro lugar.</p>"""),
    ("7. Cambios en esta política", """<p>Si cambian las prácticas de datos de la App (por ejemplo, si se añade
  analítica o funciones en línea), esta página se actualizará y se revisará la
  fecha de entrada en vigor antes de publicar el cambio. Los cambios
  importantes también se indicarán en la ficha de la tienda.</p>"""),
]

_ES_TERMS = [
    ("1. Licencia", """<p>Te concedemos una licencia personal, no exclusiva, intransferible y
  revocable para instalar y jugar a la App en dispositivos Android o iOS de tu
  propiedad o bajo tu control, para tu entretenimiento no comercial. Todos los
  derechos no concedidos expresamente quedan reservados.</p>"""),
    ("2. Publicidad", """<p>La versión gratuita muestra publicidad de terceros (Google AdMob),
  incluidos anuncios recompensados opcionales que otorgan pistas. El contenido
  publicitario lo proporcionan las redes de anuncios, no nosotros. Consulta
  nuestra <a href="privacy-es.html">Política de Privacidad</a>.</p>"""),
    ("3. Uso correcto", """<p>Te comprometes a no aplicar ingeniería inversa, descompilar ni modificar
  la App salvo cuando la ley lo permita expresamente; a no usar trucos, bots ni
  exploits; a no interferir con los mecanismos de anuncios; y a no
  usar la App de forma ilícita.</p>"""),
    ("4. Propiedad intelectual", """<p>La App — su código, niveles, puzles, arte, mascota, nombre, logotipo,
  música y sonidos — está protegida por derechos de autor y pertenece al
  desarrollador o a sus licenciantes. Estos Términos no te otorgan derecho a
  usar el nombre Chesshape ni sus recursos fuera de la App.</p>"""),
    ("5. Disponibilidad y cambios", """<p>Podemos actualizar, modificar o discontinuar la App (o cualquier función)
  en cualquier momento. Pueden requerirse
  actualizaciones para seguir jugando. Procuramos preservar el progreso entre
  actualizaciones, pero no podemos garantizarlo en toda circunstancia.</p>"""),
    ("6. Exención de garantías", """<p>La App se ofrece <strong>«tal cual» y «según disponibilidad»</strong>, sin
  garantías de ningún tipo, expresas o implícitas, incluida la idoneidad para un
  fin concreto o el funcionamiento ininterrumpido o sin errores.</p>"""),
    ("7. Limitación de responsabilidad", """<p>En la máxima medida permitida por la ley, no seremos responsables de daños
  indirectos, incidentales, especiales o consecuentes, ni de la pérdida de datos
  o progreso derivada del uso de la App. Cuando la responsabilidad no pueda
  excluirse, queda limitada en la máxima medida permitida por la ley. Nada limita los derechos
  irrenunciables que te otorga la normativa de consumo.</p>"""),
    ("8. Terminación", """<p>Estos Términos se aplican mientras uses la App. Podemos rescindir la
  licencia si los incumples de forma sustancial. Puedes terminar el acuerdo en
  cualquier momento desinstalando la App.</p>"""),
    ("9. Ley aplicable", """<p>Estos Términos se rigen por las leyes de la República de Türkiye, sin
  perjuicio de las protecciones imperativas al consumidor de tu país de
  residencia.</p>"""),
    ("10. Cambios en estos Términos", """<p>Podemos revisar estos Términos periódicamente; se actualizará la fecha de
  entrada en vigor. Seguir usando la App tras un cambio implica que aceptas los
  Términos revisados.</p>"""),
]

LANGS["es"] = _lang(
    "es", "Español", "🇪🇸",
    privacy_title="Política de Privacidad", terms_title="Términos de Uso",
    privacy_summary="Política de Privacidad del juego móvil Chesshape.",
    terms_summary="Términos de Uso del juego móvil Chesshape.",
    effective_label="Fecha de entrada en vigor", app_label="App",
    nav_home="Inicio", contact_label="Contacto",
    privacy_contact="Preguntas o solicitudes sobre privacidad:",
    terms_contact="Preguntas sobre estos Términos:",
    privacy_intro="""<p>Esta Política de Privacidad explica qué información se trata cuando juegas
  a <strong>Chesshape</strong> («la App»), un juego de puzles donde los movimientos
  de ajedrez pintan el tablero, publicado por su desarrollador independiente
  («nosotros»). En resumen: <strong>no pedimos tu nombre, correo ni ninguna
  cuenta, y no operamos servidores que almacenen tus datos.</strong> El único
  tratamiento ocurre en tu dispositivo y — para publicidad — a través
  de los servicios de Google descritos abajo.</p>""",
    privacy_sections=_ES_PRIVACY,
    terms_intro="""<p>Estos Términos de Uso («Términos») regulan tu uso del juego móvil
  <strong>Chesshape</strong> («la App»), publicado por su desarrollador
  independiente («nosotros»). Al descargar o jugar aceptas estos Términos. Si no
  estás de acuerdo, no uses la App.</p>""",
    terms_sections=_ES_TERMS,
)

_FR_PRIVACY = [
    ("1. Données stockées uniquement sur votre appareil", """<p>L'App enregistre votre progression uniquement sur votre appareil :</p>
  <ul><li>progression des niveaux, étoiles et meilleurs scores ;</li>
  <li>réglages (son, musique, vibrations, langue, accessibilité) ;</li>
  <li>solde d'indices et série du puzzle quotidien.</li></ul>
  <p>Ces données ne quittent jamais votre appareil, ne nous sont pas visibles et
  sont supprimées à la désinstallation. L'App ne lit ni vos contacts, ni vos
  photos, fichiers, position ou autre contenu personnel.</p>"""),
    ("2. Publicité (Google AdMob)", """<p>La version gratuite affiche des annonces <strong>Google AdMob</strong>. Pour
  diffuser et mesurer les annonces, Google peut traiter des données de votre
  appareil : l'<strong>identifiant publicitaire</strong>, des informations générales
  (modèle, version du système, langue), la localisation approximative (via IP)
  et les interactions publicitaires (impressions, clics).</p>
  <p>Nous ne recevons ni ne stockons aucune de ces données ; Google les traite
  selon ses propres règles. Voir la
  <a href="https://policies.google.com/privacy" rel="noopener">Politique de confidentialité de Google</a>
  et <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">comment
  Google utilise les informations des applis</a>.</p>
  <ul><li><strong>Consentement (EEE/R-U/Suisse) :</strong> le cas échéant, une fenêtre de
  consentement (Google User Messaging Platform) précède toute personnalisation ;
  vous pouvez choisir des annonces non personnalisées ou modifier vos choix à tout
  moment dans <em>Réglages → Options de confidentialité</em>.</li>
  <li><strong>Vos contrôles :</strong> les réglages publicitaires de l'appareil sont aussi
  disponibles sous Android <em>Paramètres → Confidentialité → Annonces</em> et sous iOS
  <em>Réglages → Confidentialité et sécurité → Suivi</em>.</li></ul>"""),
    ("3. Ce que nous ne faisons PAS", """<ul><li>Aucun compte, aucune inscription, aucune collecte de nom ou d'e-mail.</li>
  <li>Aucun serveur ni base de données du développeur contenant vos données.</li>
  <li>Aucune vente de données personnelles — nous n'en avons pas.</li>
  <li>Aucun SDK d'analyse tiers au-delà de la publicité décrite.</li></ul>"""),
    ("4. Enfants", """<p>L'App est un jeu de puzzle tout public. Nous ne collectons pas sciemment de
  données personnelles d'enfants. Là où des cadres de consentement s'appliquent,
  les annonces passent par les outils certifiés de Google. Si vous pensez qu'un
  enfant a fourni des données personnelles, écrivez-nous.</p>"""),
    ("5. Vos droits", """<p>Selon votre lieu de résidence (UE/EEE au titre du RGPD, Royaume-Uni,
  Californie au titre du CCPA/CPRA, Türkiye au titre de la KVKK), vous pouvez
  disposer de droits d'accès, de rectification ou d'effacement. Comme nous ne
  détenons pas de données personnelles, ces demandes concernent généralement les
  données traitées par Google — voir
  <a href="https://myadcenter.google.com" rel="noopener">Google My Ad Center</a> et les
  liens de la section 2.</p>"""),
    ("6. Sécurité et conservation", """<p>Les données de jeu résident uniquement dans le stockage privé de l'App,
  protégé par le bac à sable du système d'exploitation, et n'existent que tant que l'App est
  installée. Nous ne conservons rien après désinstallation puisque nous ne
  stockons rien ailleurs.</p>"""),
    ("7. Modifications de cette politique", """<p>Si les pratiques de données de l'App changent (ajout d'analyse ou de
  fonctions en ligne par exemple), cette page sera mise à jour et la date
  révisée avant la publication du changement. Les changements importants seront
  aussi signalés sur la fiche du store.</p>"""),
]

_FR_TERMS = [
    ("1. Licence", """<p>Nous vous accordons une licence personnelle, non exclusive, non cessible et
  révocable pour installer et jouer à l'App sur des appareils Android ou iOS que vous
  possédez ou contrôlez, pour votre divertissement non commercial. Tous les
  droits non expressément accordés nous restent réservés.</p>"""),
    ("2. Publicité", """<p>La version gratuite affiche de la publicité tierce (Google AdMob), dont des
  annonces avec récompense facultatives donnant des indices. Le contenu
  publicitaire provient des régies, pas de nous. Voir notre
  <a href="privacy-fr.html">Politique de confidentialité</a>.</p>"""),
    ("3. Usage loyal", """<p>Vous vous engagez à ne pas rétro-concevoir, décompiler ou modifier l'App
  sauf autorisation expresse de la loi ; à ne pas utiliser de triches, bots ou
  exploits ; à ne pas perturber les mécanismes de publicité ; et à ne
  pas utiliser l'App de manière illicite.</p>"""),
    ("4. Propriété intellectuelle", """<p>L'App — code, niveaux, puzzles, illustrations, mascotte, nom, logo, musique
  et sons — est protégée par le droit d'auteur et appartient au développeur ou à
  ses concédants. Ces Conditions ne vous donnent aucun droit d'utiliser le nom
  Chesshape ou ses contenus hors de l'App.</p>"""),
    ("5. Disponibilité et modifications", """<p>Nous pouvons mettre à jour, modifier ou interrompre l'App (ou toute
  fonctionnalité) à tout moment. Des mises à jour
  peuvent être nécessaires pour continuer à jouer. Nous visons à préserver la
  progression, sans pouvoir le garantir en toute circonstance.</p>"""),
    ("6. Exclusion de garanties", """<p>L'App est fournie <strong>« en l'état » et « selon disponibilité »</strong>, sans
  garantie d'aucune sorte, expresse ou implicite, y compris d'adéquation à un
  usage particulier ou de fonctionnement ininterrompu.</p>"""),
    ("7. Limitation de responsabilité", """<p>Dans la mesure maximale permise par la loi, nous ne saurions être tenus
  responsables de dommages indirects, accessoires, spéciaux ou consécutifs, ni
  de la perte de données ou de progression. Lorsque la responsabilité ne peut
  être exclue, elle reste limitée dans toute la mesure permise par la loi. Rien ne limite vos droits
  impératifs de consommateur.</p>"""),
    ("8. Résiliation", """<p>Ces Conditions s'appliquent tant que vous utilisez l'App. Nous pouvons
  résilier la licence en cas de manquement substantiel. Vous pouvez mettre fin à
  l'accord à tout moment en désinstallant l'App.</p>"""),
    ("9. Droit applicable", """<p>Ces Conditions sont régies par le droit de la République de Türkiye, sans
  préjudice des protections impératives des consommateurs de votre pays de
  résidence.</p>"""),
    ("10. Modifications des Conditions", """<p>Nous pouvons réviser ces Conditions ; la date d'entrée en vigueur sera mise
  à jour. Continuer à utiliser l'App après un changement vaut acceptation.</p>"""),
]

LANGS["fr"] = _lang(
    "fr", "Français", "🇫🇷",
    privacy_title="Politique de confidentialité", terms_title="Conditions d'utilisation",
    privacy_summary="Politique de confidentialité du jeu mobile Chesshape.",
    terms_summary="Conditions d'utilisation du jeu mobile Chesshape.",
    effective_label="Date d'entrée en vigueur", app_label="Application",
    nav_home="Accueil", contact_label="Contact",
    privacy_contact="Questions ou demandes concernant la confidentialité :",
    terms_contact="Questions sur ces Conditions :",
    privacy_intro="""<p>Cette Politique de confidentialité explique quelles informations sont
  traitées lorsque vous jouez à <strong>Chesshape</strong> (« l'App »), un jeu de
  puzzle où les coups d'échecs peignent le plateau, publié par son développeur
  indépendant (« nous »). En bref : <strong>nous ne demandons ni nom, ni e-mail,
  ni compte, et nous n'exploitons aucun serveur stockant vos données.</strong> Le
  seul traitement a lieu sur votre appareil et — pour la publicité
  — via les services Google décrits ci-dessous.</p>""",
    privacy_sections=_FR_PRIVACY,
    terms_intro="""<p>Ces Conditions d'utilisation (« Conditions ») régissent votre utilisation du
  jeu mobile <strong>Chesshape</strong> (« l'App »), publié par son développeur
  indépendant (« nous »). En téléchargeant ou en jouant, vous acceptez ces
  Conditions. Si vous ne les acceptez pas, n'utilisez pas l'App.</p>""",
    terms_sections=_FR_TERMS,
)

_IT_PRIVACY = [
    ("1. Dati salvati solo sul tuo dispositivo", """<p>L'App salva i progressi esclusivamente sul tuo dispositivo:</p>
  <ul><li>progressi dei livelli, stelle e punteggi migliori;</li>
  <li>impostazioni (audio, musica, vibrazione, lingua, accessibilità);</li>
  <li>saldo suggerimenti e serie del puzzle giornaliero.</li></ul>
  <p>Questi dati non lasciano mai il dispositivo, non sono visibili a noi e
  vengono eliminati disinstallando l'App. L'App non legge contatti, foto, file,
  posizione o altri contenuti personali.</p>"""),
    ("2. Pubblicità (Google AdMob)", """<p>La versione gratuita mostra annunci di <strong>Google AdMob</strong>. Per
  pubblicare e misurare gli annunci, Google può trattare dati del dispositivo:
  l'<strong>ID pubblicità</strong>, informazioni generali (modello, versione del
  sistema, lingua), posizione approssimativa (basata su IP) e dati di
  interazione (impression, clic).</p>
  <p>Noi non riceviamo né conserviamo tali dati; li tratta Google secondo le
  proprie norme. Vedi la
  <a href="https://policies.google.com/privacy" rel="noopener">Informativa privacy di Google</a>
  e <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">come
  Google usa le informazioni delle app</a>.</p>
  <ul><li><strong>Consenso (SEE/UK/Svizzera):</strong> ove richiesto, prima di ogni
  personalizzazione compare una finestra di consenso (Google User Messaging
  Platform); puoi scegliere annunci non personalizzati o modificare le tue scelte
  in qualsiasi momento in <em>Impostazioni → Opzioni privacy</em>.</li>
  <li><strong>I tuoi controlli:</strong> i controlli pubblicitari del dispositivo sono
  disponibili anche in Android <em>Impostazioni → Privacy → Annunci</em> e in iOS
  <em>Impostazioni → Privacy e sicurezza → Tracciamento</em>.</li></ul>"""),
    ("3. Cosa NON facciamo", """<ul><li>Nessun account, registrazione o raccolta di nomi/e-mail.</li>
  <li>Nessun server o database dello sviluppatore con i tuoi dati.</li>
  <li>Nessuna vendita di dati personali: non ne abbiamo.</li>
  <li>Nessun SDK di analisi di terze parti oltre alla pubblicità descritta.</li></ul>"""),
    ("4. Minori", """<p>L'App è un gioco di puzzle per il pubblico generale. Non raccogliamo
  consapevolmente dati personali di minori. Dove si applicano quadri di
  consenso, gli annunci passano dagli strumenti certificati di Google. Se ritieni
  che un minore abbia fornito dati personali, scrivici.</p>"""),
    ("5. I tuoi diritti", """<p>A seconda del luogo di residenza (UE/SEE con il GDPR, Regno Unito,
  California con CCPA/CPRA, Türkiye con la KVKK) puoi avere diritti di accesso,
  rettifica o cancellazione. Poiché non conserviamo dati personali, tali
  richieste riguardano di norma i dati trattati da Google — vedi
  <a href="https://myadcenter.google.com" rel="noopener">Google My Ad Center</a> e i link
  della sezione 2.</p>"""),
    ("6. Sicurezza e conservazione", """<p>I dati di gioco risiedono solo nell'archivio privato dell'App sul tuo
  dispositivo, protetto dalla sandbox applicativa del sistema operativo, ed esistono finché l'App è
  installata. Dopo la disinstallazione non conserviamo nulla perché non
  memorizziamo nulla altrove.</p>"""),
    ("7. Modifiche a questa informativa", """<p>Se le pratiche sui dati cambiano (ad esempio con analisi o funzioni
  online), questa pagina sarà aggiornata e la data rivista prima del rilascio.
  Le modifiche rilevanti saranno indicate anche nella scheda dello store.</p>"""),
]

_IT_TERMS = [
    ("1. Licenza", """<p>Ti concediamo una licenza personale, non esclusiva, non trasferibile e
  revocabile per installare e giocare all'App su dispositivi Android o iOS di tua
  proprietà o sotto il tuo controllo, per intrattenimento non commerciale. Tutti
  i diritti non espressamente concessi restano nostri.</p>"""),
    ("2. Pubblicità", """<p>La versione gratuita mostra pubblicità di terze parti (Google AdMob),
  inclusi annunci con premio facoltativi che assegnano suggerimenti. I contenuti
  pubblicitari provengono dalle reti, non da noi. Vedi la nostra
  <a href="privacy-it.html">Informativa sulla privacy</a>.</p>"""),
    ("3. Uso corretto", """<p>Ti impegni a non decompilare, disassemblare o modificare l'App salvo dove
  espressamente consentito dalla legge; a non usare cheat, bot o exploit; a non
  interferire con i meccanismi di pubblicità; e a non usare l'App in
  modo illecito.</p>"""),
    ("4. Proprietà intellettuale", """<p>L'App — codice, livelli, puzzle, grafica, mascotte, nome, logo, musica e
  suoni — è protetta dal diritto d'autore e appartiene allo sviluppatore o ai
  suoi licenzianti. Questi Termini non ti danno alcun diritto di usare il nome
  Chesshape o i contenuti al di fuori dell'App.</p>"""),
    ("5. Disponibilità e modifiche", """<p>Possiamo aggiornare, modificare o interrompere l'App (o qualsiasi funzione)
  in qualsiasi momento. Per continuare a giocare
  possono essere necessari aggiornamenti. Cerchiamo di preservare i progressi,
  ma non possiamo garantirlo in ogni circostanza.</p>"""),
    ("6. Esclusione di garanzie", """<p>L'App è fornita <strong>«così com'è» e «come disponibile»</strong>, senza garanzie
  di alcun tipo, esplicite o implicite, inclusa l'idoneità a uno scopo
  particolare o il funzionamento ininterrotto.</p>"""),
    ("7. Limitazione di responsabilità", """<p>Nella misura massima consentita dalla legge, non rispondiamo di danni
  indiretti, incidentali, speciali o consequenziali, né della perdita di dati o
  progressi. Ove la responsabilità non possa essere esclusa, è limitata nella
  misura massima consentita dalla legge.
  Nulla limita i diritti inderogabili del consumatore.</p>"""),
    ("8. Risoluzione", """<p>Questi Termini valgono finché usi l'App. Possiamo risolvere la licenza in
  caso di violazione sostanziale. Puoi terminare l'accordo in qualsiasi momento
  disinstallando l'App.</p>"""),
    ("9. Legge applicabile", """<p>Questi Termini sono regolati dalla legge della Repubblica di Türkiye, fatte
  salve le tutele imperative del consumatore del tuo paese di residenza.</p>"""),
    ("10. Modifiche ai Termini", """<p>Possiamo rivedere questi Termini; la data di entrata in vigore sarà
  aggiornata. L'uso continuato dopo una modifica ne comporta l'accettazione.</p>"""),
]

LANGS["it"] = _lang(
    "it", "Italiano", "🇮🇹",
    privacy_title="Informativa sulla privacy", terms_title="Termini di utilizzo",
    privacy_summary="Informativa sulla privacy del gioco mobile Chesshape.",
    terms_summary="Termini di utilizzo del gioco mobile Chesshape.",
    effective_label="Data di entrata in vigore", app_label="App",
    nav_home="Home", contact_label="Contatti",
    privacy_contact="Domande o richieste sulla privacy:",
    terms_contact="Domande su questi Termini:",
    privacy_intro="""<p>Questa Informativa spiega quali informazioni vengono trattate quando giochi
  a <strong>Chesshape</strong> («l'App»), un gioco di puzzle in cui le mosse degli
  scacchi dipingono la scacchiera, pubblicato dal suo sviluppatore indipendente
  («noi»). In breve: <strong>non chiediamo nome, e-mail o alcun account e non
  gestiamo server che conservino i tuoi dati.</strong> L'unico trattamento avviene
  sul tuo dispositivo e — per pubblicità — tramite i servizi Google
  descritti sotto.</p>""",
    privacy_sections=_IT_PRIVACY,
    terms_intro="""<p>Questi Termini di utilizzo («Termini») regolano l'uso del gioco mobile
  <strong>Chesshape</strong> («l'App»), pubblicato dal suo sviluppatore indipendente
  («noi»). Scaricando o giocando accetti questi Termini. In caso contrario, non
  usare l'App.</p>""",
    terms_sections=_IT_TERMS,
)

_PT_PRIVACY = [
    ("1. Dados armazenados apenas no seu dispositivo", """<p>O App guarda o seu progresso apenas no seu dispositivo:</p>
  <ul><li>progresso de níveis, estrelas e melhores pontuações;</li>
  <li>configurações (som, música, vibração, idioma, acessibilidade);</li>
  <li>saldo de dicas e sequência do quebra-cabeça diário.</li></ul>
  <p>Esses dados nunca saem do seu dispositivo, não são visíveis para nós e são
  apagados ao desinstalar o App. O App não lê seus contatos, fotos, arquivos,
  localização nem qualquer outro conteúdo pessoal.</p>"""),
    ("2. Publicidade (Google AdMob)", """<p>A versão gratuita exibe anúncios do <strong>Google AdMob</strong>. Para veicular
  e medir anúncios, o Google pode tratar dados do seu dispositivo: o
  <strong>ID de publicidade</strong>, informações gerais (modelo, versão do sistema,
  idioma), localização aproximada (por IP) e dados de interação (impressões,
  cliques).</p>
  <p>Não recebemos nem armazenamos esses dados; o Google os trata conforme suas
  próprias políticas. Veja a
  <a href="https://policies.google.com/privacy" rel="noopener">Política de Privacidade do Google</a>
  e <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">como
  o Google usa informações de apps</a>.</p>
  <ul><li><strong>Consentimento (EEE/RU/Suíça):</strong> quando exigido, uma janela de
  consentimento (Google User Messaging Platform) aparece antes de qualquer
  personalização; você pode escolher anúncios não personalizados ou alterar suas
  escolhas a qualquer momento em <em>Configurações → Opções de privacidade</em>.</li>
  <li><strong>Seus controles:</strong> os controles publicitários do dispositivo também
  estão disponíveis no Android em <em>Configurações → Privacidade → Anúncios</em> e no iOS
  em <em>Ajustes → Privacidade e Segurança → Rastreamento</em>.</li></ul>"""),
    ("3. O que NÃO fazemos", """<ul><li>Sem contas, cadastros ou coleta de nomes/e-mails.</li>
  <li>Sem servidores ou bancos de dados do desenvolvedor com seus dados.</li>
  <li>Sem venda de dados pessoais — não temos nenhum.</li>
  <li>Sem SDKs de análise de terceiros além da publicidade descrita.</li></ul>"""),
    ("4. Crianças", """<p>O App é um jogo de quebra-cabeça para público geral. Não coletamos
  intencionalmente dados pessoais de crianças. Onde se aplicam estruturas de
  consentimento, os anúncios são solicitados pelas ferramentas certificadas do
  Google. Se acredita que uma criança forneceu dados pessoais, fale conosco.</p>"""),
    ("5. Seus direitos", """<p>Dependendo de onde você mora (UE/EEE sob o GDPR, Reino Unido, Califórnia
  sob CCPA/CPRA, Türkiye sob a KVKK), você pode ter direitos de acesso,
  correção ou exclusão. Como não guardamos dados pessoais, esses pedidos em
  geral dizem respeito a dados tratados pelo Google — veja
  <a href="https://myadcenter.google.com" rel="noopener">Google My Ad Center</a> e os links
  da seção 2.</p>"""),
    ("6. Segurança e retenção", """<p>Os dados de jogo ficam apenas no armazenamento privado do App no seu
  dispositivo, protegido pelo sandbox de aplicativos do sistema operacional, e existem enquanto o App
  estiver instalado. Nada é retido após a desinstalação porque nada é guardado
  em outro lugar.</p>"""),
    ("7. Alterações desta política", """<p>Se as práticas de dados do App mudarem (por exemplo, com análise ou
  recursos on-line), esta página será atualizada e a data revisada antes do
  lançamento. Mudanças relevantes também serão indicadas na página da loja.</p>"""),
]

_PT_TERMS = [
    ("1. Licença", """<p>Concedemos a você uma licença pessoal, não exclusiva, intransferível e
  revogável para instalar e jogar o App em dispositivos Android ou iOS que você possua
  ou controle, para entretenimento não comercial. Todos os direitos não
  concedidos expressamente permanecem conosco.</p>"""),
    ("2. Publicidade", """<p>A versão gratuita exibe publicidade de terceiros (Google AdMob), incluindo
  anúncios premiados opcionais que concedem dicas. O conteúdo dos anúncios vem
  das redes, não de nós. Veja nossa
  <a href="privacy-pt.html">Política de Privacidade</a>.</p>"""),
    ("3. Uso justo", """<p>Você concorda em não fazer engenharia reversa, descompilar ou modificar o
  App, exceto quando a lei permitir expressamente; não usar cheats, bots ou
  exploits; não interferir nos mecanismos de anúncios; e não usar o
  App de forma ilegal.</p>"""),
    ("4. Propriedade intelectual", """<p>O App — código, níveis, quebra-cabeças, arte, mascote, nome, logotipo,
  música e sons — é protegido por direitos autorais e pertence ao desenvolvedor
  ou seus licenciadores. Estes Termos não lhe dão direito de usar o nome
  Chesshape ou seus recursos fora do App.</p>"""),
    ("5. Disponibilidade e mudanças", """<p>Podemos atualizar, alterar ou descontinuar o App (ou qualquer recurso)
  a qualquer momento. Atualizações podem ser
  necessárias para continuar jogando. Buscamos preservar o progresso, mas não
  podemos garanti-lo em toda circunstância.</p>"""),
    ("6. Isenção de garantias", """<p>O App é fornecido <strong>"no estado em que se encontra" e "conforme
  disponível"</strong>, sem garantias de qualquer tipo, expressas ou implícitas,
  incluindo adequação a uma finalidade específica ou operação ininterrupta.</p>"""),
    ("7. Limitação de responsabilidade", """<p>Na máxima extensão permitida por lei, não seremos responsáveis por danos
  indiretos, incidentais, especiais ou consequenciais, nem por perda de dados ou
  progresso. Onde a responsabilidade não puder ser excluída, fica limitada na
  máxima extensão permitida por lei. Nada limita
  direitos irrenunciáveis do consumidor.</p>"""),
    ("8. Rescisão", """<p>Estes Termos valem enquanto você usar o App. Podemos rescindir a licença em
  caso de violação substancial. Você pode encerrar o acordo a qualquer momento
  desinstalando o App.</p>"""),
    ("9. Lei aplicável", """<p>Estes Termos são regidos pelas leis da República da Türkiye, sem prejuízo
  das proteções imperativas ao consumidor do seu país de residência.</p>"""),
    ("10. Alterações destes Termos", """<p>Podemos revisar estes Termos; a data de vigência será atualizada. Continuar
  usando o App após uma alteração significa que você aceita os Termos
  revisados.</p>"""),
]

LANGS["pt"] = _lang(
    "pt", "Português", "🇵🇹",
    privacy_title="Política de Privacidade", terms_title="Termos de Uso",
    privacy_summary="Política de Privacidade do jogo móvel Chesshape.",
    terms_summary="Termos de Uso do jogo móvel Chesshape.",
    effective_label="Data de vigência", app_label="App", nav_home="Início",
    contact_label="Contato",
    privacy_contact="Dúvidas ou solicitações sobre privacidade:",
    terms_contact="Dúvidas sobre estes Termos:",
    privacy_intro="""<p>Esta Política de Privacidade explica quais informações são tratadas quando
  você joga <strong>Chesshape</strong> ("o App"), um jogo de quebra-cabeça em que
  movimentos de xadrez pintam o tabuleiro, publicado por seu desenvolvedor
  independente ("nós"). Em resumo: <strong>não pedimos seu nome, e-mail ou
  qualquer conta, e não operamos servidores que armazenem seus dados.</strong> O
  único tratamento ocorre no seu dispositivo e — para publicidade —
  pelos serviços do Google descritos abaixo.</p>""",
    privacy_sections=_PT_PRIVACY,
    terms_intro="""<p>Estes Termos de Uso ("Termos") regem o uso do jogo móvel
  <strong>Chesshape</strong> ("o App"), publicado por seu desenvolvedor independente
  ("nós"). Ao baixar ou jogar, você concorda com estes Termos. Se não concordar,
  não use o App.</p>""",
    terms_sections=_PT_TERMS,
)

_RU_PRIVACY = [
    ("1. Данные, хранящиеся только на вашем устройстве", """<p>Приложение сохраняет игровой прогресс только на вашем устройстве:</p>
  <ul><li>прогресс уровней, звёзды и лучшие результаты;</li>
  <li>настройки (звук, музыка, вибрация, язык, доступность);</li>
  <li>запас подсказок и серия ежедневных головоломок.</li></ul>
  <p>Эти данные никогда не покидают устройство, недоступны нам и удаляются при
  удалении Приложения. Приложение не читает контакты, фотографии, файлы,
  местоположение и иное личное содержимое.</p>"""),
    ("2. Реклама (Google AdMob)", """<p>Бесплатная версия показывает рекламу <strong>Google AdMob</strong>. Для показа и
  измерения рекламы Google может обрабатывать данные вашего устройства:
  <strong>рекламный идентификатор</strong>, общие сведения об устройстве (модель,
  версия ОС, язык), примерное местоположение (по IP) и данные о взаимодействии
  с рекламой (показы, клики).</p>
  <p>Мы не получаем и не храним эти данные; их обрабатывает Google по
  собственным правилам. Подробнее — в
  <a href="https://policies.google.com/privacy" rel="noopener">Политике конфиденциальности Google</a>
  и <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">о том,
  как Google использует данные приложений</a>.</p>
  <ul><li><strong>Согласие (ЕЭЗ/Великобритания/Швейцария):</strong> где требуется, перед
  персонализацией показывается окно согласия (Google User Messaging Platform);
  вы можете выбрать неперсонализированную рекламу или в любое время изменить
  выбор в <em>Настройки → Параметры конфиденциальности</em>.</li>
  <li><strong>Ваш контроль:</strong> настройки рекламы на уровне устройства также доступны
  в Android <em>Настройки → Конфиденциальность → Реклама</em> и iOS
  <em>Настройки → Конфиденциальность и безопасность → Отслеживание</em>.</li></ul>"""),
    ("3. Чего мы НЕ делаем", """<ul><li>Никаких аккаунтов, регистраций и сбора имён или адресов электронной почты.</li>
  <li>Никаких серверов или баз данных разработчика с вашими данными.</li>
  <li>Никакой продажи персональных данных — их у нас нет.</li>
  <li>Никаких сторонних аналитических SDK помимо описанной рекламы.</li></ul>"""),
    ("4. Дети", """<p>Приложение — головоломка для широкой аудитории. Мы сознательно не собираем
  персональные данные детей. Там, где применяются рамки согласия, реклама
  запрашивается через сертифицированные инструменты Google. Если вы считаете,
  что ребёнок передал персональные данные, напишите нам.</p>"""),
    ("5. Ваши права", """<p>В зависимости от места проживания (ЕС/ЕЭЗ по GDPR, Великобритания,
  Калифорния по CCPA/CPRA, Türkiye по KVKK) у вас могут быть права на доступ,
  исправление или удаление данных. Поскольку мы не храним персональные данные,
  такие запросы обычно касаются данных, обрабатываемых Google — см.
  <a href="https://myadcenter.google.com" rel="noopener">Google My Ad Center</a> и ссылки
  в разделе 2.</p>"""),
    ("6. Безопасность и хранение", """<p>Игровые данные находятся только в приватном хранилище Приложения на вашем
  устройстве, защищённом песочницей приложений операционной системы, и существуют, пока установлено
  Приложение. После удаления у нас ничего не остаётся, потому что мы ничего не
  храним в другом месте.</p>"""),
    ("7. Изменения политики", """<p>Если практики обработки данных изменятся (например, появится аналитика или
  сетевые функции), эта страница будет обновлена, а дата вступления в силу
  изменена до выпуска. О существенных изменениях также будет указано в
  описании в магазине.</p>"""),
]

_RU_TERMS = [
    ("1. Лицензия", """<p>Мы предоставляем вам личную, неисключительную, непередаваемую и отзывную
  лицензию на установку и игру в Приложение на устройствах Android или iOS, которыми вы
  владеете или управляете, для некоммерческого развлечения. Все права, прямо не
  предоставленные, остаются за нами.</p>"""),
    ("2. Реклама", """<p>Бесплатная версия показывает стороннюю рекламу (Google AdMob), включая
  необязательную рекламу с вознаграждением, дающую подсказки. Содержание
  рекламы предоставляют рекламные сети, а не мы. См.
  <a href="privacy-ru.html">Политику конфиденциальности</a>.</p>"""),
    ("3. Добросовестное использование", """<p>Вы соглашаетесь не декомпилировать, не подвергать обратной разработке и не
  изменять Приложение, кроме случаев, прямо разрешённых законом; не использовать
  читы, ботов или эксплойты; не вмешиваться в механизмы рекламы; не
  использовать Приложение противоправно.</p>"""),
    ("4. Интеллектуальная собственность", """<p>Приложение — код, уровни, головоломки, графика, маскот, название, логотип,
  музыка и звуки — защищено авторским правом и принадлежит разработчику или его
  лицензиарам. Эти Условия не дают права использовать название Chesshape или его
  материалы вне Приложения.</p>"""),
    ("5. Доступность и изменения", """<p>Мы можем обновлять, изменять или прекращать поддержку Приложения (или
  любой функции) в любое время. Для продолжения
  игры могут потребоваться обновления. Мы стремимся сохранять прогресс, но не
  можем гарантировать это в любых технических обстоятельствах.</p>"""),
    ("6. Отказ от гарантий", """<p>Приложение предоставляется <strong>«как есть» и «как доступно»</strong>, без
  каких-либо гарантий, явных или подразумеваемых, включая пригодность для
  конкретной цели и бесперебойную работу.</p>"""),
    ("7. Ограничение ответственности", """<p>В максимально допустимой законом степени мы не несём ответственности за
  косвенные, случайные, особые или последующие убытки, а также за потерю данных или
  прогресса. Там, где ответственность нельзя исключить, она ограничена в
  максимально допустимой законом степени. Ничто
  не ограничивает неотчуждаемые права потребителя.</p>"""),
    ("8. Прекращение", """<p>Эти Условия действуют, пока вы пользуетесь Приложением. Мы можем прекратить
  лицензию при существенном нарушении. Вы можете прекратить соглашение в любой
  момент, удалив Приложение.</p>"""),
    ("9. Применимое право", """<p>Эти Условия регулируются законодательством Турецкой Республики, без ущерба
  для императивных норм защиты прав потребителей страны вашего проживания.</p>"""),
    ("10. Изменения Условий", """<p>Мы можем время от времени пересматривать эти Условия; дата вступления в
  силу будет обновлена. Продолжение использования после изменения означает
  согласие с новой редакцией.</p>"""),
]

LANGS["ru"] = _lang(
    "ru", "Русский", "🇷🇺",
    privacy_title="Политика конфиденциальности", terms_title="Условия использования",
    privacy_summary="Политика конфиденциальности мобильной игры Chesshape.",
    terms_summary="Условия использования мобильной игры Chesshape.",
    effective_label="Дата вступления в силу", app_label="Приложение",
    nav_home="Главная", contact_label="Контакты",
    privacy_contact="Вопросы или запросы о конфиденциальности:",
    terms_contact="Вопросы по этим Условиям:",
    privacy_intro="""<p>Эта Политика объясняет, какие сведения обрабатываются, когда вы играете в
  <strong>Chesshape</strong> («Приложение») — головоломку, где ходы шахматных фигур
  закрашивают доску, выпущенную независимым разработчиком («мы»). Коротко:
  <strong>мы не спрашиваем имя, электронную почту или аккаунт и не держим
  серверов, хранящих ваши данные.</strong> Обработка происходит только на вашем
  устройстве и — для рекламы — через сервисы Google, описанные
  ниже.</p>""",
    privacy_sections=_RU_PRIVACY,
    terms_intro="""<p>Эти Условия использования («Условия») регулируют использование мобильной
  игры <strong>Chesshape</strong> («Приложение»), выпущенной независимым
  разработчиком («мы»). Загружая Приложение или играя в него, вы принимаете эти
  Условия. Если вы не согласны, не используйте Приложение.</p>""",
    terms_sections=_RU_TERMS,
)

_ID_PRIVACY = [
    ("1. Data yang hanya disimpan di perangkat Anda", """<p>Aplikasi menyimpan kemajuan permainan hanya di perangkat Anda:</p>
  <ul><li>kemajuan level, bintang, dan skor terbaik;</li>
  <li>pengaturan (suara, musik, getaran, bahasa, aksesibilitas);</li>
  <li>saldo petunjuk dan rentetan teka-teki harian.</li></ul>
  <p>Data ini tidak pernah meninggalkan perangkat Anda, tidak terlihat oleh kami,
  dan terhapus saat Aplikasi dicopot. Aplikasi tidak membaca kontak, foto,
  berkas, lokasi, atau konten pribadi lainnya.</p>"""),
    ("2. Iklan (Google AdMob)", """<p>Versi gratis menampilkan iklan dari <strong>Google AdMob</strong>. Untuk
  menayangkan dan mengukur iklan, Google dapat memproses data perangkat Anda:
  <strong>ID Iklan</strong>, informasi umum perangkat (model, versi sistem, bahasa),
  lokasi perkiraan (berbasis IP), dan data interaksi iklan (tayangan, klik).</p>
  <p>Kami tidak menerima maupun menyimpan data tersebut; Google memprosesnya
  menurut kebijakannya sendiri. Lihat
  <a href="https://policies.google.com/privacy" rel="noopener">Kebijakan Privasi Google</a>
  dan <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">cara
  Google menggunakan informasi dari aplikasi</a>.</p>
  <ul><li><strong>Persetujuan (EEA/UK/Swiss):</strong> bila diwajibkan, dialog persetujuan
  (Google User Messaging Platform) ditampilkan sebelum personalisasi; Anda dapat
  memilih iklan non-personalisasi atau mengubah pilihan kapan saja di
  <em>Setelan → Opsi Privasi</em>.</li>
  <li><strong>Kendali Anda:</strong> kontrol iklan tingkat perangkat juga tersedia di
  Android <em>Setelan → Privasi → Iklan</em> dan iOS
  <em>Pengaturan → Privasi &amp; Keamanan → Pelacakan</em>.</li></ul>"""),
    ("3. Yang TIDAK kami lakukan", """<ul><li>Tanpa akun, pendaftaran, atau pengumpulan nama/e-mail.</li>
  <li>Tanpa server atau basis data pengembang yang menyimpan data Anda.</li>
  <li>Tanpa penjualan data pribadi — kami tidak memilikinya.</li>
  <li>Tanpa SDK analitik pihak ketiga selain periklanan di atas.</li></ul>"""),
    ("4. Anak-anak", """<p>Aplikasi adalah gim teka-teki untuk umum. Kami tidak dengan sengaja
  mengumpulkan data pribadi anak. Bila kerangka persetujuan berlaku, iklan
  diminta melalui alat bersertifikat Google. Jika Anda yakin seorang anak telah
  memberikan data pribadi, hubungi kami.</p>"""),
    ("5. Hak Anda", """<p>Bergantung pada tempat tinggal Anda (UE/EEA di bawah GDPR, Inggris,
  California di bawah CCPA/CPRA, Türkiye di bawah KVKK), Anda mungkin memiliki
  hak akses, perbaikan, atau penghapusan. Karena kami tidak menyimpan data
  pribadi, permintaan semacam itu umumnya menyangkut data yang diproses Google —
  lihat <a href="https://myadcenter.google.com" rel="noopener">Google My Ad Center</a> dan
  tautan di bagian 2.</p>"""),
    ("6. Keamanan &amp; penyimpanan", """<p>Data permainan hanya berada di penyimpanan privat Aplikasi pada perangkat
  Anda, dilindungi sandbox aplikasi sistem operasi, dan ada selama Aplikasi terpasang. Kami tidak
  menyimpan apa pun setelah pencopotan karena kami tidak menyimpan apa pun di
  tempat lain.</p>"""),
    ("7. Perubahan kebijakan ini", """<p>Jika praktik data Aplikasi berubah (misalnya analitik atau fitur daring
  ditambahkan), halaman ini akan diperbarui dan tanggal berlaku direvisi sebelum
  perubahan dirilis. Perubahan penting juga dicatat di halaman toko.</p>"""),
]

_ID_TERMS = [
    ("1. Lisensi", """<p>Kami memberi Anda lisensi pribadi, non-eksklusif, tidak dapat dialihkan,
  dan dapat dicabut untuk memasang dan memainkan Aplikasi pada perangkat Android atau iOS
  yang Anda miliki atau kendalikan, untuk hiburan non-komersial. Semua hak yang
  tidak diberikan secara tegas tetap pada kami.</p>"""),
    ("2. Periklanan", """<p>Versi gratis menampilkan iklan pihak ketiga (Google AdMob), termasuk iklan
  berhadiah opsional yang memberi petunjuk. Konten iklan berasal dari jaringan
  iklan, bukan dari kami. Lihat
  <a href="privacy-id.html">Kebijakan Privasi</a> kami.</p>"""),
    ("3. Penggunaan wajar", """<p>Anda setuju untuk tidak merekayasa balik, mendekompilasi, atau memodifikasi
  Aplikasi kecuali diizinkan hukum; tidak memakai cheat, bot, atau eksploit;
  tidak mengganggu mekanisme iklan; dan tidak menggunakan
  Aplikasi secara melanggar hukum.</p>"""),
    ("4. Kekayaan intelektual", """<p>Aplikasi — kode, level, teka-teki, karya seni, maskot, nama, logo, musik,
  dan suara — dilindungi hak cipta dan dimiliki pengembang atau pemberi
  lisensinya. Ketentuan ini tidak memberi Anda hak memakai nama Chesshape atau
  asetnya di luar Aplikasi.</p>"""),
    ("5. Ketersediaan &amp; perubahan", """<p>Kami dapat memperbarui, mengubah, atau menghentikan Aplikasi (atau fitur apa
  pun) kapan saja. Pembaruan mungkin diperlukan untuk
  terus bermain. Kami berupaya menjaga kemajuan pemain namun tidak dapat
  menjaminnya dalam setiap keadaan teknis.</p>"""),
    ("6. Penafian jaminan", """<p>Aplikasi disediakan <strong>"sebagaimana adanya" dan "sebagaimana
  tersedia"</strong>, tanpa jaminan apa pun, tersurat maupun tersirat, termasuk
  kesesuaian untuk tujuan tertentu atau operasi tanpa gangguan.</p>"""),
    ("7. Pembatasan tanggung jawab", """<p>Sejauh diizinkan hukum, kami tidak bertanggung jawab atas kerugian tidak
  langsung, insidental, khusus, atau konsekuensial, maupun kehilangan data atau
  kemajuan. Bila tanggung jawab tidak dapat dikecualikan, tanggung jawab tersebut
  dibatasi sejauh diizinkan oleh hukum. Hak konsumen yang tidak dapat dilepaskan tetap
  berlaku.</p>"""),
    ("8. Pengakhiran", """<p>Ketentuan ini berlaku selama Anda menggunakan Aplikasi. Kami dapat
  mengakhiri lisensi jika Anda melanggar secara material. Anda dapat mengakhiri
  perjanjian kapan saja dengan mencopot Aplikasi.</p>"""),
    ("9. Hukum yang berlaku", """<p>Ketentuan ini diatur oleh hukum Republik Türkiye, tanpa mengurangi
  perlindungan konsumen yang bersifat memaksa di negara tempat tinggal Anda.</p>"""),
    ("10. Perubahan Ketentuan", """<p>Kami dapat merevisi Ketentuan ini dari waktu ke waktu; tanggal berlaku di
  atas akan diperbarui. Penggunaan berkelanjutan setelah perubahan berarti Anda
  menerima Ketentuan yang direvisi.</p>"""),
]

LANGS["id"] = _lang(
    "id", "Bahasa Indonesia", "🇮🇩",
    privacy_title="Kebijakan Privasi", terms_title="Ketentuan Penggunaan",
    privacy_summary="Kebijakan Privasi untuk gim seluler Chesshape.",
    terms_summary="Ketentuan Penggunaan untuk gim seluler Chesshape.",
    effective_label="Tanggal berlaku", app_label="Aplikasi", nav_home="Beranda",
    contact_label="Kontak",
    privacy_contact="Pertanyaan atau permintaan tentang privasi:",
    terms_contact="Pertanyaan tentang Ketentuan ini:",
    privacy_intro="""<p>Kebijakan Privasi ini menjelaskan informasi apa yang ditangani saat Anda
  memainkan <strong>Chesshape</strong> ("Aplikasi"), gim teka-teki tempat langkah
  catur mewarnai papan, yang diterbitkan oleh pengembang independennya ("kami").
  Singkatnya: <strong>kami tidak meminta nama, e-mail, atau akun apa pun, dan kami
  tidak menjalankan server yang menyimpan data Anda.</strong> Pemrosesan hanya
  terjadi di perangkat Anda dan — untuk iklan — melalui layanan
  Google di bawah ini.</p>""",
    privacy_sections=_ID_PRIVACY,
    terms_intro="""<p>Ketentuan Penggunaan ini ("Ketentuan") mengatur penggunaan gim seluler
  <strong>Chesshape</strong> ("Aplikasi"), yang diterbitkan oleh pengembang
  independennya ("kami"). Dengan mengunduh atau memainkan Aplikasi, Anda
  menyetujui Ketentuan ini. Jika tidak setuju, mohon jangan gunakan Aplikasi.</p>""",
    terms_sections=_ID_TERMS,
)

_JA_PRIVACY = [
    ("1. 端末内にのみ保存されるデータ", """<p>本アプリはゲームの状態をお客様の端末内にのみ保存します。</p>
  <ul><li>レベルの進行状況、スター、ベストスコア</li>
  <li>設定（効果音、音楽、触覚フィードバック、言語、アクセシビリティ）</li>
  <li>ヒント残数、デイリーパズルの連続記録</li></ul>
  <p>これらのデータが端末外に出ることはなく、当方からは参照できません。アプリを
  アンインストールすると削除されます。本アプリは連絡先、写真、ファイル、位置情報
  その他の個人的な内容を読み取りません。</p>"""),
    ("2. 広告（Google AdMob）", """<p>無料版では <strong>Google AdMob</strong> による広告を表示します。広告の配信と
  測定のため、Google は端末上の次のデータを処理する場合があります:
  <strong>広告 ID</strong>、一般的な端末情報（機種、OS バージョン、言語）、
  おおよその位置情報（IP ベース）、広告の操作データ（表示、クリック）。</p>
  <p>当方はこれらのデータを受け取らず、保存もしません。Google が自社のポリシーに
  基づき処理します。詳細は
  <a href="https://policies.google.com/privacy" rel="noopener">Google プライバシー ポリシー</a>
  および <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Google
  がアプリから得た情報を使用する方法</a>をご覧ください。</p>
  <ul><li><strong>同意（EEA/英国/スイス）:</strong> 必要な地域では、広告のパーソナライズ前に
  同意ダイアログ（Google User Messaging Platform）が表示され、非パーソナライズ
  広告を選択できます。アプリの<em>設定 → プライバシーオプション</em>からいつでも
  選択を変更できます。</li>
  <li><strong>お客様による管理:</strong> 端末側の広告設定は Android の
  <em>設定 → プライバシー → 広告</em>および iOS の
  <em>設定 → プライバシーとセキュリティ → トラッキング</em>でも利用できます。</li></ul>"""),
    ("3. 当方が行わないこと", """<ul><li>アカウント、登録、氏名・メールアドレスの収集は行いません。</li>
  <li>お客様のデータを保持する開発者運用のサーバーやデータベースはありません。</li>
  <li>個人情報の販売は行いません。保有していません。</li>
  <li>上記の広告以外にサードパーティの解析 SDK は使用していません。</li></ul>"""),
    ("4. 子ども", """<p>本アプリは一般向けのパズルゲームです。子どもから個人情報を意図的に収集する
  ことはありません。同意フレームワークが適用される地域では、Google の認定ツールを
  通じて広告をリクエストします。お子様が個人情報を提供したと思われる場合はご連絡
  ください。</p>"""),
    ("5. お客様の権利", """<p>お住まいの地域（GDPR に基づく EU/EEA、英国、CCPA/CPRA に基づくカリフォルニア、
  KVKK に基づくトルコなど）により、アクセス・訂正・削除の権利が認められる場合が
  あります。当方は個人データを保持していないため、こうした請求は通常 Google が
  処理するデータに関わります。
  <a href="https://myadcenter.google.com" rel="noopener">Google 広告センター</a>および
  第 2 項のリンクをご覧ください。</p>"""),
    ("6. セキュリティとデータ保持", """<p>ゲームデータは OS のアプリサンドボックスで保護された端末内のプライベート
  領域にのみ存在し、アプリがインストールされている間だけ保持されます。他の場所に
  保存していないため、アンインストール後に当方に残るものはありません。</p>"""),
    ("7. 本ポリシーの変更", """<p>本アプリのデータの取り扱いが変わる場合（解析やオンライン機能の追加など）、
  変更の提供前に本ページを更新し、発効日を改めます。重要な変更はストアの掲載情報
  にも記載します。</p>"""),
]

_JA_TERMS = [
    ("1. ライセンス", """<p>当方は、お客様が所有または管理する Android または iOS 端末に本アプリをインストールし、
  非商業的な娯楽目的で利用するための、個人的・非独占的・譲渡不可・撤回可能な
  ライセンスを付与します。明示的に付与されない権利はすべて当方に留保されます。</p>"""),
    ("2. 広告", """<p>無料版では第三者の広告（Google AdMob）を表示します。ヒントを得られる任意の
  リワード広告も含まれます。広告の内容は当方ではなく広告ネットワークが提供します。
  広告に使われるデータについては<a href="privacy-ja.html">プライバシーポリシー</a>を
  ご覧ください。</p>"""),
    ("3. 公正な利用", """<p>お客様は次の行為を行わないことに同意します: 法律が明示的に認める場合を除く
  リバースエンジニアリング、逆コンパイル、改変。チート、ボット、エクスプロイトの
  使用。広告の仕組みへの妨害。違法な方法での利用。</p>"""),
    ("4. 知的財産", """<p>本アプリ（コード、レベル、パズル、アートワーク、マスコット、名称、ロゴ、音楽、
  効果音を含む）は著作権その他の法律で保護され、開発者またはそのライセンサーに
  帰属します。本規約は、本アプリ外で Chesshape の名称や素材を使用する権利を
  与えるものではありません。</p>"""),
    ("5. 提供状況と変更", """<p>当方はいつでも本アプリ（任意の機能）を更新、変更、提供終了
  することがあります。継続してプレイするために更新が必要になる場合があります。
  更新をまたいで進行状況の保持に努めますが、あらゆる技術的状況で保証はできません。</p>"""),
    ("6. 保証の否認", """<p>本アプリは<strong>「現状有姿」および「提供可能な範囲」</strong>で提供され、特定目的
  への適合性や中断・エラーのない動作を含め、明示黙示を問わずいかなる保証も
  行いません。</p>"""),
    ("7. 責任の制限", """<p>適用法が認める最大限の範囲で、当方は本アプリの利用に起因する間接的・付随的・
  特別・結果的損害、またはデータや進行状況の損失について責任を負いません。責任を
  排除できない場合も、適用法で認められる最大限の範囲に制限されます。放棄できない消費者の権利は制限されません。</p>"""),
    ("8. 終了", """<p>本規約はお客様が本アプリを利用する間、適用されます。重大な違反があった場合、
  当方はライセンスを終了できます。お客様はアプリをアンインストールすることでいつでも
  契約を終了できます。</p>"""),
    ("9. 準拠法", """<p>本規約はトルコ共和国の法律に準拠します。お客様の居住国の強行的な消費者保護は
  妨げられません。</p>"""),
    ("10. 本規約の変更", """<p>当方は本規約を随時改定することがあり、上記の発効日を更新します。変更後も本
  アプリを利用し続けた場合、改定後の規約に同意したものとみなされます。</p>"""),
]

LANGS["ja"] = _lang(
    "ja", "日本語", "🇯🇵",
    privacy_title="プライバシーポリシー", terms_title="利用規約",
    privacy_summary="モバイルゲーム Chesshape のプライバシーポリシー。",
    terms_summary="モバイルゲーム Chesshape の利用規約。",
    effective_label="発効日", app_label="アプリ", nav_home="ホーム",
    contact_label="お問い合わせ",
    privacy_contact="プライバシーに関するご質問・ご依頼:",
    terms_contact="本規約に関するご質問:",
    privacy_intro="""<p>本プライバシーポリシーは、チェスの駒の動きで盤面を塗るパズルゲーム
  <strong>Chesshape</strong>（以下「本アプリ」）を、独立開発者（以下「当方」）が
  提供するにあたり、どのような情報が扱われるかを説明します。要点は次のとおりです:
  <strong>お名前・メールアドレス・アカウントを一切お尋ねせず、お客様のデータを保存する
  サーバーも運用していません。</strong> データ処理はお客様の端末内、および広告に
  ついては下記の Google のサービスを通じてのみ行われます。</p>""",
    privacy_sections=_JA_PRIVACY,
    terms_intro="""<p>本利用規約（以下「本規約」）は、独立開発者（以下「当方」）が提供するモバイル
  ゲーム <strong>Chesshape</strong>（以下「本アプリ」）の利用について定めます。本アプリを
  ダウンロードまたはプレイすることで、本規約に同意したものとみなされます。同意
  されない場合は本アプリをご利用にならないでください。</p>""",
    terms_sections=_JA_TERMS,
)

_KO_PRIVACY = [
    ("1. 기기에만 저장되는 데이터", """<p>앱은 게임 상태를 오직 사용자의 기기에만 저장합니다.</p>
  <ul><li>레벨 진행도, 별, 최고 기록</li>
  <li>설정(소리, 음악, 진동, 언어, 접근성)</li>
  <li>힌트 잔액, 일일 퍼즐 연속 기록</li></ul>
  <p>이 데이터는 기기를 벗어나지 않으며 저희가 볼 수 없고, 앱을 삭제하면 함께
  지워집니다. 앱은 연락처, 사진, 파일, 위치 등 어떤 개인 콘텐츠도 읽지 않습니다.</p>"""),
    ("2. 광고(Google AdMob)", """<p>무료 버전에는 <strong>Google AdMob</strong> 광고가 표시됩니다. 광고 게재와 측정을
  위해 Google은 기기의 <strong>광고 ID</strong>, 일반 기기 정보(모델, OS 버전, 언어),
  대략적인 위치(IP 기반), 광고 상호작용 데이터(노출, 클릭)를 처리할 수 있습니다.</p>
  <p>저희는 이 데이터를 받지도 저장하지도 않으며, Google이 자체 정책에 따라
  처리합니다. 자세한 내용은
  <a href="https://policies.google.com/privacy" rel="noopener">Google 개인정보처리방침</a>과
  <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Google이
  앱 정보를 사용하는 방식</a>을 참고하세요.</p>
  <ul><li><strong>동의(EEA/영국/스위스):</strong> 필요한 경우 광고 개인 맞춤 전에 동의 창
  (Google User Messaging Platform)이 표시되며, 비개인 맞춤 광고를 선택할 수 있습니다.
  앱의 <em>설정 → 개인정보 보호 옵션</em>에서 언제든지 선택을 변경할 수 있습니다.</li>
  <li><strong>사용자 제어:</strong> 기기 수준 광고 설정은 Android
  <em>설정 → 개인정보 보호 → 광고</em> 및 iOS
  <em>설정 → 개인정보 보호 및 보안 → 추적</em>에서도 사용할 수 있습니다.</li></ul>"""),
    ("3. 저희가 하지 않는 것", """<ul><li>계정, 가입, 이름·이메일 수집이 없습니다.</li>
  <li>사용자의 데이터를 보관하는 개발자 서버나 데이터베이스가 없습니다.</li>
  <li>개인정보 판매가 없습니다 — 보유한 것이 없습니다.</li>
  <li>위 광고 외에 제3자 분석 SDK를 사용하지 않습니다.</li></ul>"""),
    ("4. 아동", """<p>본 앱은 전체 이용가 퍼즐 게임입니다. 저희는 아동의 개인정보를 고의로
  수집하지 않습니다. 동의 체계가 적용되는 지역에서는 Google의 인증 도구를 통해
  광고를 요청합니다. 아동이 개인정보를 제공했다고 생각되면 연락해 주세요.</p>"""),
    ("5. 사용자의 권리", """<p>거주 지역(GDPR에 따른 EU/EEA, 영국, CCPA/CPRA에 따른 캘리포니아, KVKK에 따른
  튀르키예 등)에 따라 열람·정정·삭제 권리를 가질 수 있습니다. 저희는 개인정보를
  보유하지 않으므로 이러한 요청은 대개 Google이 처리하는 데이터와 관련됩니다 —
  <a href="https://myadcenter.google.com" rel="noopener">Google 내 광고 센터</a>와 2항의
  링크를 참고하세요.</p>"""),
    ("6. 보안 및 보관", """<p>게임 데이터는 운영 체제의 앱 샌드박스로 보호되는 기기 내 앱 전용 저장소에만
  존재하며, 앱이 설치되어 있는 동안에만 유지됩니다. 다른 곳에 저장하지 않으므로
  삭제 후 저희에게 남는 것은 없습니다.</p>"""),
    ("7. 본 방침의 변경", """<p>앱의 데이터 처리 방식이 바뀌면(예: 분석 또는 온라인 기능 추가) 변경 배포 전에
  이 페이지를 갱신하고 발효일을 수정합니다. 중요한 변경은 스토어 등록정보에도
  표시합니다.</p>"""),
]

_KO_TERMS = [
    ("1. 라이선스", """<p>저희는 사용자가 소유하거나 관리하는 Android 또는 iOS 기기에 앱을 설치하고 비상업적
  용도로 플레이할 수 있는 개인적·비독점적·양도 불가·철회 가능한 라이선스를
  부여합니다. 명시적으로 부여되지 않은 모든 권리는 저희에게 있습니다.</p>"""),
    ("2. 광고", """<p>무료 버전에는 제3자 광고(Google AdMob)가 표시되며, 힌트를 제공하는 선택적
  보상형 광고가 포함됩니다. 광고 콘텐츠는 저희가 아니라 광고 네트워크가
  제공합니다. 광고에 사용되는 데이터는
  <a href="privacy-ko.html">개인정보처리방침</a>을 참고하세요.</p>"""),
    ("3. 공정한 이용", """<p>사용자는 법이 명시적으로 허용하는 경우를 제외하고 앱을 역설계·디컴파일·수정
  하지 않으며, 치트·봇·익스플로잇을 사용하지 않고, 광고 메커니즘을 방해하지
  않으며, 불법적인 방식으로 앱을 사용하지 않을 것에 동의합니다.</p>"""),
    ("4. 지식재산권", """<p>앱(코드, 레벨, 퍼즐, 아트워크, 마스코트, 이름, 로고, 음악, 사운드 포함)은
  저작권 등으로 보호되며 개발자 또는 그 라이선서에게 귀속됩니다. 본 약관은 앱
  외부에서 Chesshape 이름이나 자산을 사용할 권리를 부여하지 않습니다.</p>"""),
    ("5. 제공 및 변경", """<p>저희는 언제든지 앱(모든 기능)을 업데이트·변경·중단할 수
  있습니다. 계속 플레이하려면 업데이트가 필요할 수 있습니다. 업데이트 전반에 걸쳐
  진행도를 보존하려 노력하지만 모든 기술적 상황에서 보장할 수는 없습니다.</p>"""),
    ("6. 보증의 부인", """<p>앱은 <strong>"있는 그대로" 및 "이용 가능한 상태로"</strong> 제공되며, 특정 목적
  적합성이나 중단·오류 없는 작동을 포함하여 명시적이든 묵시적이든 어떠한 보증도
  하지 않습니다.</p>"""),
    ("7. 책임의 제한", """<p>관련 법이 허용하는 최대 범위에서, 저희는 앱 사용으로 인한 간접적·부수적·특별·
  결과적 손해나 데이터·진행도의 손실에 대해 책임지지 않습니다. 책임을 배제할 수
  없는 경우에도 관련 법이 허용하는 최대 범위로 제한됩니다.
  포기할 수 없는 소비자 권리는 제한되지 않습니다.</p>"""),
    ("8. 해지", """<p>본 약관은 사용자가 앱을 사용하는 동안 적용됩니다. 중대한 위반이 있는 경우
  저희는 라이선스를 해지할 수 있습니다. 사용자는 앱을 삭제하여 언제든지 계약을
  종료할 수 있습니다.</p>"""),
    ("9. 준거법", """<p>본 약관은 튀르키예 공화국 법률의 적용을 받으며, 거주 국가의 강행적 소비자
  보호 규정을 침해하지 않습니다.</p>"""),
    ("10. 약관의 변경", """<p>저희는 본 약관을 수시로 개정할 수 있으며 위의 발효일이 갱신됩니다. 변경 후
  계속 앱을 사용하면 개정된 약관에 동의한 것으로 봅니다.</p>"""),
]

LANGS["ko"] = _lang(
    "ko", "한국어", "🇰🇷",
    privacy_title="개인정보처리방침", terms_title="이용약관",
    privacy_summary="모바일 게임 Chesshape의 개인정보처리방침.",
    terms_summary="모바일 게임 Chesshape의 이용약관.",
    effective_label="발효일", app_label="앱", nav_home="홈",
    contact_label="문의",
    privacy_contact="개인정보 관련 문의 및 요청:",
    terms_contact="본 약관에 관한 문의:",
    privacy_intro="""<p>본 개인정보처리방침은 체스 기물의 움직임으로 보드를 칠하는 퍼즐 게임
  <strong>Chesshape</strong>(이하 "앱")를 독립 개발자(이하 "저희")가 제공함에 있어 어떤
  정보가 처리되는지 설명합니다. 요약하면: <strong>저희는 이름, 이메일, 계정을 전혀
  요구하지 않으며 사용자의 데이터를 저장하는 서버도 운영하지 않습니다.</strong> 모든
  처리는 사용자의 기기에서, 그리고 광고에 한해 아래에 설명된 Google
  서비스를 통해 이루어집니다.</p>""",
    privacy_sections=_KO_PRIVACY,
    terms_intro="""<p>본 이용약관(이하 "약관")은 독립 개발자(이하 "저희")가 제공하는 모바일 게임
  <strong>Chesshape</strong>(이하 "앱")의 이용에 적용됩니다. 앱을 다운로드하거나
  플레이하면 본 약관에 동의한 것으로 간주됩니다. 동의하지 않으시면 앱을 이용하지
  말아 주세요.</p>""",
    terms_sections=_KO_TERMS,
)


# ------------------------------------------------ purchase-aware normalization
#
# The language tables above deliberately keep the original editorial blocks
# readable.  This final normalization is the single parity boundary for facts
# that must never drift between locales: platform backup behavior and the
# client-only in-app-purchase flow.  build.py renders LANGS only after this
# block has replaced the former device-only wording and inserted the same new
# sections in every language.

_PURCHASE_COPY = {
    "en": {
        "privacy_intro": """<p>This Privacy Policy explains what information is handled when you play
  <strong>Chesshape</strong> ("the App"), a chess-move painting puzzle game
  published by its independent developer ("we", "us"). The short version:
  <strong>we do not ask for your name, e-mail or an account, and we do not run
  a server that stores your game or purchase records.</strong> Game and purchase-
  delivery records are handled locally; Google processes advertising data; and
  Apple App Store or Google Play processes payments, as described below.</p>""",
        "local_heading": "1. Local game and purchase records",
        "local_body": """<p>The App keeps the following records in its private local storage:</p>
  <ul><li>level progress, stars, best scores, settings, language and accessibility choices;</li>
  <li>hint balance and daily-puzzle streak;</li>
  <li>Premium entitlement and a compact transaction-delivery marker used to prevent duplicate grants.</li></ul>
  <p>The App does not store a full store receipt, payment-card details or store
  credentials. These local records are not visible to us. Depending on your OS,
  account and device settings, Apple or Google backup/device-transfer features
  may copy or restore them. Uninstalling normally removes the device copy, but
  does not guarantee deletion of a platform backup that may later restore it.
  The App does not read contacts, photos, files, precise location or other
  personal content.</p>""",
        "payment_heading": "3. In-app purchases and payment data",
        "payment_body": """<p>In-app purchases are processed by <strong>Apple App Store</strong> on iOS
  and <strong>Google Play</strong> on Android under their own terms and privacy
  policies. We do not receive your payment-card details or billing credentials.
  To deliver a product and restore Premium, the native billing SDK temporarily
  provides the App with a store receipt or purchase token, product identifier,
  purchase status, transaction date and reference. These values are not sent to
  a developer-operated server; the App retains only the compact one-way delivery
  fingerprint described in Section 1. Refund and revocation requests are handled
  by the store.
  This client-only release has no authoritative server-side reconciliation: the
  App may learn of a change only if the store later reports it and may not detect
  or revoke local Premium/content promptly or at all. Consumed hints cannot be
  reliably clawed back. The App stores only the local entitlement/balance and
  compact delivery marker described in Section 1.</p>""",
        "security_heading": "7. Security, retention and backup",
        "security_body": """<p>Local game and purchase-delivery records are protected by the operating
  system's application sandbox. They normally remain while the App is installed
  and may also be included in an OS backup or device transfer controlled by you
  and the platform. Removing the App usually removes its local copy; a platform
  backup may restore it later. We retain no copy on a developer-operated server.</p>""",
        "terms_heading": "3. In-app purchases",
        "terms_body": """<p>The App offers the following optional products through Apple App Store
  or Google Play:</p>
  <ul><li><code>premium_no_ads</code> is a non-consumable purchase that enables
  Premium and removes ads. Its first eligible original purchase includes a
  one-time bonus of 25 hints. Restoring Premium is supported, but a fresh
  restore does not issue that one-time bonus again.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code> and
  <code>hints_100</code> are consumable hint packs.</li></ul>
  <p>There are <strong>no subscriptions</strong>. The store controls and displays
  the final localized price, currency and applicable taxes before confirmation;
  the price shown by the store governs. Purchases are also subject to that
  store's terms.</p>
  <p>Premium can be restored through the same store account. Stores do not
  restore consumed hint packs across devices or reinstalls, and Chesshape has
  no account/server that can recreate them. A remaining local hint balance may
  reappear only if the operating system happens to restore the App's local data,
  which is not guaranteed. Refund and revocation requests are decided and
  processed by Apple or Google. This client-only release has no authoritative
  server reconciliation, so the App may not receive, detect or reflect that
  change promptly or at all; consumed hints cannot be reliably clawed back.
  Nothing here limits non-waivable consumer rights.</p>""",
    },
    "tr": {
        "privacy_intro": """<p>Bu Gizlilik Politikası, bağımsız geliştiricisi ("biz") tarafından yayımlanan
  satranç hamleleriyle boyama bulmacası <strong>Chesshape</strong> ("Uygulama")
  oynanırken hangi bilgilerin işlendiğini açıklar. Kısaca: <strong>adınızı,
  e-postanızı veya hesap bilgisi istemiyoruz; oyun ya da satın alma kayıtlarınızı
  tutan bir sunucu işletmiyoruz.</strong> Oyun ve satın alma teslim kayıtları
  cihazda işlenir; reklam verilerini Google, ödemeleri ise aşağıda açıklandığı
  üzere Apple App Store veya Google Play işler.</p>""",
        "local_heading": "1. Yerel oyun ve satın alma kayıtları",
        "local_body": """<p>Uygulama aşağıdaki kayıtları kendisine ait özel yerel alanda tutar:</p>
  <ul><li>bölüm ilerlemesi, yıldızlar, en iyi skorlar, ayarlar, dil ve erişilebilirlik tercihleri;</li>
  <li>ipucu bakiyesi ve günlük bulmaca serisi;</li>
  <li>Premium hakkı ve aynı ürünün iki kez verilmesini önleyen küçük bir işlem-teslim işareti.</li></ul>
  <p>Uygulama tam mağaza makbuzunu, ödeme kartı bilgilerini veya mağaza giriş
  bilgilerini saklamaz. Bu yerel kayıtlar bizim tarafımızdan görülemez. İşletim
  sistemi, hesap ve cihaz ayarlarınıza bağlı olarak Apple veya Google yedekleme/
  cihaz aktarımı bunları kopyalayabilir ya da geri yükleyebilir. Uygulamayı
  kaldırmak cihazdaki kopyayı normalde siler; daha sonra geri gelebilecek bir
  platform yedeğinin silinmesini garanti etmez. Uygulama kişilerinizi,
  fotoğraflarınızı, dosyalarınızı, kesin konumunuzu veya başka kişisel içeriği okumaz.</p>""",
        "payment_heading": "3. Uygulama içi satın almalar ve ödeme verileri",
        "payment_body": """<p>Uygulama içi satın almalar iOS'ta <strong>Apple App Store</strong>,
  Android'de <strong>Google Play</strong> tarafından kendi şartları ve gizlilik
  politikaları kapsamında işlenir. Kart bilgilerinizi veya ödeme giriş
  bilgilerinizi almayız. Ürünü teslim etmek ve Premium'u geri yüklemek için yerel
  faturalandırma SDK'sı mağaza makbuzu ya da satın alma token'ını, ürün kimliğini,
  satın alma durumunu, tarihini ve işlem referansını geçici olarak Uygulamaya
  iletir. Bunlar geliştirici sunucusuna gönderilmez; Uygulama yalnızca 1. bölümde
  açıklanan tek yönlü küçük teslim parmak izini saklar. İade ve iptalleri mağaza
  işler. Yalnızca istemcide
  çalışan bu sürümde yetkili bir sunucu mutabakatı yoktur: Uygulama değişikliği
  ancak mağaza daha sonra bildirirse öğrenebilir; yerel Premium/içeriği zamanında
  veya hiç iptal edemeyebilir. Tüketilmiş ipuçları güvenilir biçimde geri
  alınamaz. Uygulama yalnızca 1. bölümdeki yerel hak/bakiye ve küçük teslim
  işaretini saklar.</p>""",
        "security_heading": "7. Güvenlik, saklama ve yedekleme",
        "security_body": """<p>Yerel oyun ve satın alma teslim kayıtları işletim sisteminin uygulama
  korumalı alanıyla korunur. Normalde Uygulama kurulu olduğu sürece kalırlar;
  ayrıca sizin ve platformun denetimindeki işletim sistemi yedeğine veya cihaz
  aktarımına dâhil edilebilirler. Kaldırma işlemi yerel kopyayı genellikle siler,
  ancak platform yedeği daha sonra geri yükleyebilir. Geliştirici sunucusunda
  hiçbir kopya tutmayız.</p>""",
        "terms_heading": "3. Uygulama içi satın almalar",
        "terms_body": """<p>Uygulama, Apple App Store veya Google Play üzerinden şu isteğe bağlı
  ürünleri sunar:</p>
  <ul><li><code>premium_no_ads</code>, Premium'u etkinleştirip reklamları kaldıran
  tüketilmeyen bir üründür. Uygun ilk özgün satın alma bir defaya mahsus 25 ipucu
  bonusu içerir. Premium geri yüklenebilir; ancak yeni kurulumdaki geri yükleme
  bu tek seferlik bonusu yeniden vermez.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code> ve
  <code>hints_100</code> tüketilebilir ipucu paketleridir.</li></ul>
  <p><strong>Abonelik yoktur.</strong> Onaydan önce gösterilen nihai yerel fiyatı,
  para birimini ve geçerli vergileri mağaza belirler; mağazanın gösterdiği fiyat
  geçerlidir. Satın almalar ilgili mağazanın şartlarına da tabidir.</p>
  <p>Premium aynı mağaza hesabıyla geri yüklenebilir. Mağazalar tüketilmiş ipucu
  paketlerini cihazlar veya yeniden kurulumlar arasında geri yüklemez; Chesshape'in
  bunları yeniden oluşturacak hesabı ya da sunucusu yoktur. Kalan yerel ipucu
  bakiyesi yalnızca işletim sistemi Uygulamanın yerel verisini geri yüklerse
  yeniden görünebilir; bu garanti edilmez. İade ve iptal taleplerini Apple veya
  Google karara bağlayıp işler. Bu istemci tabanlı sürümde yetkili sunucu
  mutabakatı olmadığından Uygulama değişikliği zamanında veya hiç alamayabilir,
  algılamayabilir ya da yansıtamayabilir; tüketilmiş ipuçları güvenilir biçimde
  geri alınamaz. Buradaki hiçbir hüküm vazgeçilemez tüketici haklarını sınırlamaz.</p>""",
    },
    "de": {
        "privacy_intro": """<p>Diese Datenschutzerklärung erläutert, welche Informationen beim Spielen
  von <strong>Chesshape</strong> („App") verarbeitet werden. <strong>Wir fragen
  weder Namen noch E-Mail-Adresse oder Konto ab und betreiben keinen Server,
  der Spiel- oder Kaufdaten speichert.</strong> Spiel- und Auslieferungsdaten
  werden lokal verarbeitet; Google verarbeitet Werbedaten; Zahlungen werden
  wie unten beschrieben vom Apple App Store oder von Google Play verarbeitet.</p>""",
        "local_heading": "1. Lokale Spiel- und Kaufdaten",
        "local_body": """<p>Die App speichert in ihrem privaten lokalen Bereich:</p>
  <ul><li>Levelfortschritt, Sterne, Bestwerte, Einstellungen, Sprache und Barrierefreiheit;</li>
  <li>Tipp-Guthaben und Tagesrätsel-Serie;</li>
  <li>Premium-Berechtigung und eine kompakte Transaktions-/Auslieferungsmarke gegen doppelte Gutschriften.</li></ul>
  <p>Vollständige Store-Belege, Zahlungskartendaten oder Store-Zugangsdaten
  werden nicht gespeichert. Diese lokalen Daten sind für uns nicht einsehbar.
  Je nach Betriebssystem-, Konto- und Geräteeinstellungen können Apple- oder
  Google-Sicherung und Geräteübertragung sie kopieren oder wiederherstellen.
  Eine Deinstallation entfernt gewöhnlich die Gerätekopie, garantiert aber
  nicht die Löschung einer später wiederherstellbaren Plattform-Sicherung. Die
  App liest keine Kontakte, Fotos, Dateien, genauen Standortdaten oder sonstigen persönlichen Inhalte.</p>""",
        "payment_heading": "3. In-App-Käufe und Zahlungsdaten",
        "payment_body": """<p>In-App-Käufe werden unter iOS vom <strong>Apple App Store</strong> und
  unter Android von <strong>Google Play</strong> nach deren Bedingungen und
  Datenschutzregeln verarbeitet. Wir erhalten keine Kartendaten oder Zahlungs-
  zugangsdaten. Für Auslieferung und Premium-Wiederherstellung stellt das native
  Abrechnungs-SDK der App vorübergehend einen Store-Beleg oder Kauf-Token sowie
  Produktkennung, Kaufstatus, Datum und Transaktionsreferenz bereit. Diese Werte
  werden nicht an einen Entwickler-Server gesendet; gespeichert bleibt nur der
  kompakte Einweg-Auslieferungsfingerabdruck aus Abschnitt 1. Erstattungen und
  Widerrufe bearbeitet der Store. Diese rein clientseitige Version hat keinen maßgeblichen Server-
  abgleich: Die App erfährt eine Änderung nur, wenn der Store sie später meldet,
  und erkennt bzw. entzieht lokales Premium/Inhalte unter Umständen verspätet
  oder gar nicht. Verbrauchte Tipps können nicht zuverlässig zurückgebucht
  werden. Gespeichert werden nur Berechtigung/Guthaben und die kompakte Marke aus Abschnitt 1.</p>""",
        "security_heading": "7. Sicherheit, Speicherdauer und Sicherung",
        "security_body": """<p>Lokale Spiel- und Auslieferungsdaten schützt die App-Sandbox des
  Betriebssystems. Sie bleiben normalerweise während der Installation bestehen
  und können in eine von Ihnen und der Plattform gesteuerte OS-Sicherung oder
  Geräteübertragung einfließen. Die Deinstallation entfernt meist die lokale
  Kopie; eine Plattform-Sicherung kann sie später wiederherstellen. Auf einem
  vom Entwickler betriebenen Server behalten wir keine Kopie.</p>""",
        "terms_heading": "3. In-App-Käufe",
        "terms_body": """<p>Die App bietet über Apple App Store oder Google Play optional:</p>
  <ul><li><code>premium_no_ads</code> ist ein nicht verbrauchbarer Kauf, der Premium
  aktiviert und Werbung entfernt. Der erste berechtigte Originalkauf enthält
  einmalig 25 Tipps. Premium kann wiederhergestellt werden; eine frische
  Wiederherstellung gewährt diesen Einmalbonus nicht erneut.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code> und
  <code>hints_100</code> sind verbrauchbare Tipp-Pakete.</li></ul>
  <p>Es gibt <strong>keine Abonnements</strong>. Der Store bestimmt und zeigt vor
  Bestätigung den endgültigen lokalisierten Preis, die Währung und anfallende
  Steuern; maßgeblich ist der Store-Preis. Es gelten zusätzlich die Store-Bedingungen.</p>
  <p>Premium lässt sich mit demselben Store-Konto wiederherstellen. Verbrauchte
  Tipp-Pakete stellen Stores nicht geräte- oder installationsübergreifend wieder
  her; Chesshape hat kein Konto/Server, der sie neu erzeugt. Ein lokales
  Restguthaben erscheint nur wieder, falls das Betriebssystem die lokalen
  App-Daten wiederherstellt, was nicht garantiert ist. Erstattungen und
  Widerrufe entscheidet und verarbeitet Apple bzw. Google. Ohne maßgeblichen
  Serverabgleich empfängt, erkennt oder berücksichtigt die App diese Änderung
  unter Umständen verspätet oder gar nicht; verbrauchte Tipps können nicht
  zuverlässig zurückgebucht werden. Unabdingbare Verbraucherrechte bleiben unberührt.</p>""",
    },
    "es": {
        "privacy_intro": """<p>Esta Política de Privacidad explica qué información se trata al jugar a
  <strong>Chesshape</strong> («la App»). <strong>No pedimos nombre, correo ni
  cuenta, ni operamos un servidor que guarde datos de juego o compras.</strong>
  Los registros de juego y entrega se tratan localmente; Google trata datos
  publicitarios; y Apple App Store o Google Play procesa los pagos como se
  explica a continuación.</p>""",
        "local_heading": "1. Registros locales de juego y compras",
        "local_body": """<p>La App conserva en su almacenamiento local privado:</p>
  <ul><li>progreso, estrellas, mejores puntuaciones, ajustes, idioma y accesibilidad;</li>
  <li>saldo de pistas y racha del puzle diario;</li>
  <li>derecho Premium y una marca compacta de transacción/entrega que evita concesiones duplicadas.</li></ul>
  <p>No guarda el recibo completo de la tienda, datos de tarjeta ni credenciales
  de la tienda. No podemos ver estos registros locales. Según los ajustes del
  sistema, cuenta y dispositivo, las funciones de copia o transferencia de
  Apple o Google pueden copiarlos o restaurarlos. Desinstalar suele borrar la
  copia del dispositivo, pero no garantiza eliminar una copia de plataforma
  que pueda restaurarse después. La App no lee contactos, fotos, archivos,
  ubicación precisa ni otro contenido personal.</p>""",
        "payment_heading": "3. Compras dentro de la App y datos de pago",
        "payment_body": """<p>Las compras son procesadas por <strong>Apple App Store</strong> en iOS y
  <strong>Google Play</strong> en Android conforme a sus términos y políticas.
  No recibimos datos de tarjeta ni credenciales de facturación. Para entregar
  un producto y restaurar Premium, el SDK de facturación nativo facilita
  temporalmente a la App un recibo o token de compra, el identificador del
  producto, estado, fecha y referencia de la transacción. Estos valores no se
  envían a un servidor del desarrollador; solo se conserva la huella compacta
  unidireccional de entrega indicada en la sección 1. La tienda gestiona
  reembolsos y revocaciones. Esta versión solo cliente no tiene
  conciliación autorizada en servidor: la App conocerá un cambio únicamente si
  la tienda lo comunica después, y puede no detectar o retirar Premium/contenido
  local a tiempo o nunca. Las pistas consumidas no pueden recuperarse de forma
  fiable. La App solo conserva el derecho/saldo y la marca compacta de la sección 1.</p>""",
        "security_heading": "7. Seguridad, conservación y copias",
        "security_body": """<p>El sandbox del sistema protege los registros locales de juego y entrega.
  Normalmente permanecen mientras la App está instalada y pueden incluirse en
  una copia del sistema o transferencia controlada por ti y la plataforma.
  Desinstalar suele eliminar la copia local; una copia de plataforma puede
  restaurarla más tarde. No guardamos copia en un servidor del desarrollador.</p>""",
        "terms_heading": "3. Compras dentro de la App",
        "terms_body": """<p>La App ofrece opcionalmente mediante Apple App Store o Google Play:</p>
  <ul><li><code>premium_no_ads</code> es una compra no consumible que activa
  Premium y elimina anuncios. La primera compra original apta incluye una sola
  bonificación de 25 pistas. Premium puede restaurarse, pero una restauración
  nueva no vuelve a conceder esa bonificación.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code> y
  <code>hints_100</code> son paquetes consumibles de pistas.</li></ul>
  <p><strong>No hay suscripciones.</strong> La tienda controla y muestra antes de
  confirmar el precio localizado final, moneda e impuestos; prevalece ese
  precio. También se aplican los términos de la tienda.</p>
  <p>Premium se restaura con la misma cuenta de tienda. Las tiendas no restauran
  paquetes consumidos entre dispositivos o reinstalaciones, y Chesshape no tiene
  cuenta/servidor que los recree. Un saldo local restante solo podría reaparecer
  si el sistema restaura los datos locales, sin garantía. Apple o Google decide
  y procesa reembolsos y revocaciones. Sin conciliación autorizada en servidor,
  la App puede no recibir, detectar o reflejar el cambio a tiempo o nunca; las
  pistas consumidas no pueden recuperarse de forma fiable. No se limitan
  derechos irrenunciables del consumidor.</p>""",
    },
    "fr": {
        "privacy_intro": """<p>Cette Politique explique les informations traitées lorsque vous jouez à
  <strong>Chesshape</strong> (« l'App »). <strong>Nous ne demandons ni nom, ni
  e-mail, ni compte et n'exploitons aucun serveur stockant les données de jeu
  ou d'achat.</strong> Les registres de jeu et de livraison sont traités
  localement ; Google traite les données publicitaires ; Apple App Store ou
  Google Play traite les paiements comme décrit ci-dessous.</p>""",
        "local_heading": "1. Registres locaux de jeu et d'achat",
        "local_body": """<p>L'App conserve dans son stockage local privé :</p>
  <ul><li>progression, étoiles, scores, réglages, langue et accessibilité ;</li>
  <li>solde d'indices et série du puzzle quotidien ;</li>
  <li>droit Premium et marque compacte de transaction/livraison empêchant une double attribution.</li></ul>
  <p>Elle ne stocke ni reçu complet du store, ni carte de paiement, ni identifiants
  du store. Nous ne voyons pas ces registres locaux. Selon les réglages du
  système, du compte et de l'appareil, la sauvegarde ou le transfert Apple/Google
  peut les copier ou les restaurer. Désinstaller supprime normalement la copie
  de l'appareil, sans garantir la suppression d'une sauvegarde de plateforme
  restaurable ultérieurement. L'App ne lit ni contacts, photos, fichiers,
  position précise ou autre contenu personnel.</p>""",
        "payment_heading": "3. Achats intégrés et données de paiement",
        "payment_body": """<p>Les achats sont traités par <strong>Apple App Store</strong> sous iOS et
  <strong>Google Play</strong> sous Android selon leurs propres conditions et
  politiques. Nous ne recevons ni carte ni identifiants de facturation. Pour la
  livraison et la restauration de Premium, le SDK de paiement natif fournit
  temporairement à l'App un reçu ou jeton d'achat, l'identifiant produit, l'état,
  la date et la référence de transaction. Ces valeurs ne sont pas envoyées à un
  serveur du développeur ; seule l'empreinte de livraison compacte à sens unique
  décrite à la section 1 est conservée. Le store traite restitutions et
  révocations. Cette version uniquement
  côté client ne dispose d'aucun rapprochement serveur faisant autorité : l'App
  ne connaît un changement que si le store le signale plus tard et peut ne pas
  détecter ni retirer Premium/contenu local rapidement, voire jamais. Les indices
  consommés ne peuvent pas être repris de façon fiable. L'App ne garde que le
  droit/solde et la marque compacte de la section 1.</p>""",
        "security_heading": "7. Sécurité, conservation et sauvegarde",
        "security_body": """<p>Le bac à sable du système protège les registres locaux de jeu et de
  livraison. Ils demeurent normalement pendant l'installation et peuvent être
  inclus dans une sauvegarde ou un transfert contrôlé par vous et la plateforme.
  Désinstaller supprime généralement la copie locale ; une sauvegarde de
  plateforme peut la restaurer. Aucun exemplaire n'est conservé sur un serveur du développeur.</p>""",
        "terms_heading": "3. Achats intégrés",
        "terms_body": """<p>L'App propose en option via Apple App Store ou Google Play :</p>
  <ul><li><code>premium_no_ads</code> est un achat non consommable activant
  Premium et supprimant les publicités. Le premier achat original admissible
  comprend un bonus unique de 25 indices. Premium peut être restauré, mais une
  nouvelle restauration ne redonne pas ce bonus.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code> et
  <code>hints_100</code> sont des lots d'indices consommables.</li></ul>
  <p>Il n'existe <strong>aucun abonnement</strong>. Le store contrôle et affiche
  avant confirmation le prix localisé final, la devise et les taxes ; ce prix
  prévaut. Ses conditions s'appliquent également.</p>
  <p>Premium se restaure avec le même compte de store. Les stores ne restaurent
  pas les lots consommés entre appareils ou réinstallations et Chesshape n'a
  aucun compte/serveur pour les recréer. Un solde local restant ne peut réapparaître
  que si le système restaure les données locales, sans garantie. Apple ou Google
  décide et traite restitutions et révocations. Sans rapprochement serveur
  faisant autorité, l'App peut ne pas recevoir, détecter ou refléter ce changement
  rapidement, voire jamais ; les indices consommés ne peuvent pas être repris de
  façon fiable. Les droits impératifs du consommateur restent inchangés.</p>""",
    },
    "it": {
        "privacy_intro": """<p>Questa Informativa spiega quali informazioni vengono trattate giocando a
  <strong>Chesshape</strong> (l'“App”). <strong>Non chiediamo nome, e-mail o
  account e non gestiamo server che conservano dati di gioco o acquisto.</strong>
  I registri di gioco e consegna sono trattati localmente; Google tratta dati
  pubblicitari; Apple App Store o Google Play tratta i pagamenti come descritto sotto.</p>""",
        "local_heading": "1. Registri locali di gioco e acquisto",
        "local_body": """<p>L'App conserva nell'archivio locale privato:</p>
  <ul><li>progressi, stelle, record, impostazioni, lingua e accessibilità;</li>
  <li>saldo degli aiuti e serie del puzzle giornaliero;</li>
  <li>diritto Premium e un indicatore compatto di transazione/consegna contro accrediti duplicati.</li></ul>
  <p>Non salva la ricevuta completa dello store, dati della carta o credenziali
  dello store. Non possiamo vedere questi registri locali. Secondo le impostazioni
  di sistema, account e dispositivo, backup o trasferimento Apple/Google può
  copiarli o ripristinarli. Disinstallare elimina normalmente la copia sul
  dispositivo, ma non garantisce l'eliminazione di un backup di piattaforma
  ripristinabile. L'App non legge contatti, foto, file, posizione precisa o altri contenuti personali.</p>""",
        "payment_heading": "3. Acquisti in-app e dati di pagamento",
        "payment_body": """<p>Gli acquisti sono elaborati da <strong>Apple App Store</strong> su iOS e
  <strong>Google Play</strong> su Android secondo i rispettivi termini e
  informative. Non riceviamo dati della carta né credenziali di pagamento. Per
  consegna e ripristino Premium, l'SDK di fatturazione nativo fornisce
  temporaneamente all'App una ricevuta o un token d'acquisto, ID prodotto, stato,
  data e riferimento della transazione. Questi valori non vengono inviati a un
  server dello sviluppatore; resta solo l'impronta compatta unidirezionale di
  consegna descritta nella sezione 1. Rimborsi e revoche sono gestiti dallo
  store. Questa versione solo client non ha una riconciliazione
  server autorevole: l'App può conoscere una modifica solo se lo store la segnala
  in seguito e potrebbe non rilevare o revocare Premium/contenuti locali
  tempestivamente o mai. Gli aiuti consumati non possono essere recuperati in
  modo affidabile. L'App conserva solo diritto/saldo e indicatore compatto della sezione 1.</p>""",
        "security_heading": "7. Sicurezza, conservazione e backup",
        "security_body": """<p>La sandbox del sistema protegge i registri locali di gioco e consegna.
  Restano normalmente durante l'installazione e possono entrare in backup o
  trasferimenti controllati dall'utente e dalla piattaforma. Disinstallare
  elimina di solito la copia locale; un backup della piattaforma può ripristinarla.
  Non conserviamo copie su server gestiti dallo sviluppatore.</p>""",
        "terms_heading": "3. Acquisti in-app",
        "terms_body": """<p>L'App offre facoltativamente tramite Apple App Store o Google Play:</p>
  <ul><li><code>premium_no_ads</code> è un acquisto non consumabile che attiva
  Premium e rimuove la pubblicità. Il primo acquisto originale idoneo include un
  bonus una tantum di 25 aiuti. Premium è ripristinabile, ma un ripristino su una
  nuova installazione non concede nuovamente il bonus.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code> e
  <code>hints_100</code> sono pacchetti consumabili di aiuti.</li></ul>
  <p>Non ci sono <strong>abbonamenti</strong>. Lo store controlla e mostra prima
  della conferma prezzo localizzato finale, valuta e imposte; prevale il prezzo
  dello store. Si applicano anche i suoi termini.</p>
  <p>Premium è ripristinabile con lo stesso account dello store. Gli store non
  ripristinano pacchetti consumati tra dispositivi o reinstallazioni e Chesshape
  non ha account/server per ricrearli. Un saldo locale residuo può ricomparire
  solo se il sistema ripristina i dati locali, senza garanzia. Apple o Google
  decide ed elabora rimborsi e revoche. Senza riconciliazione server autorevole,
  l'App potrebbe non ricevere, rilevare o riflettere la modifica tempestivamente
  o mai; gli aiuti consumati non possono essere recuperati in modo affidabile.
  Restano fermi i diritti inderogabili del consumatore.</p>""",
    },
    "pt": {
        "privacy_intro": """<p>Esta Política explica as informações tratadas ao jogar
  <strong>Chesshape</strong> (o “App”). <strong>Não pedimos nome, e-mail ou conta
  e não operamos servidor que guarde dados de jogo ou compra.</strong> Registros
  de jogo e entrega são tratados localmente; o Google trata dados publicitários;
  Apple App Store ou Google Play processa pagamentos conforme abaixo.</p>""",
        "local_heading": "1. Registros locais de jogo e compra",
        "local_body": """<p>O App mantém no armazenamento local privado:</p>
  <ul><li>progresso, estrelas, recordes, configurações, idioma e acessibilidade;</li>
  <li>saldo de dicas e sequência do puzzle diário;</li>
  <li>direito Premium e marcador compacto de transação/entrega contra concessões duplicadas.</li></ul>
  <p>Não guarda recibo completo da loja, dados de cartão ou credenciais da loja.
  Não vemos esses registros locais. Conforme configurações do sistema, conta e
  dispositivo, backup ou transferência Apple/Google pode copiá-los ou restaurá-los.
  Desinstalar normalmente remove a cópia do dispositivo, mas não garante apagar
  backup da plataforma restaurável depois. O App não lê contatos, fotos,
  arquivos, localização precisa nem outro conteúdo pessoal.</p>""",
        "payment_heading": "3. Compras no App e dados de pagamento",
        "payment_body": """<p>Compras são processadas pela <strong>Apple App Store</strong> no iOS e
  <strong>Google Play</strong> no Android conforme seus termos e políticas. Não
  recebemos cartão nem credenciais de cobrança. Para entrega e restauração
  Premium, o SDK de faturamento nativo fornece temporariamente ao App um recibo
  ou token de compra, ID do produto, estado, data e referência da transação.
  Esses valores não são enviados a servidor do desenvolvedor; permanece apenas
  a impressão digital compacta e unidirecional de entrega descrita na seção 1.
  A loja trata reembolsos e revogações. Esta
  versão somente cliente não tem conciliação oficial no servidor: o App só pode
  saber da mudança se a loja a informar depois e talvez não detecte ou revogue
  Premium/conteúdo local prontamente ou nunca. Dicas consumidas não podem ser
  recuperadas com confiança. O App guarda apenas direito/saldo e marcador compacto da seção 1.</p>""",
        "security_heading": "7. Segurança, retenção e backup",
        "security_body": """<p>O sandbox do sistema protege registros locais de jogo e entrega. Eles
  normalmente permanecem durante a instalação e podem integrar backup ou
  transferência controlada por você e pela plataforma. Desinstalar costuma
  remover a cópia local; backup da plataforma pode restaurá-la. Não guardamos
  cópia em servidor operado pelo desenvolvedor.</p>""",
        "terms_heading": "3. Compras no App",
        "terms_body": """<p>O App oferece opcionalmente pela Apple App Store ou Google Play:</p>
  <ul><li><code>premium_no_ads</code> é compra não consumível que ativa Premium e
  remove anúncios. A primeira compra original elegível inclui bônus único de 25
  dicas. Premium pode ser restaurado, mas uma restauração nova não concede o
  bônus outra vez.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code> e
  <code>hints_100</code> são pacotes consumíveis de dicas.</li></ul>
  <p><strong>Não há assinaturas.</strong> A loja controla e mostra antes da
  confirmação preço localizado final, moeda e impostos; vale o preço da loja.
  Também se aplicam os termos dela.</p>
  <p>Premium é restaurável com a mesma conta da loja. Lojas não restauram pacotes
  consumidos entre dispositivos ou reinstalações e Chesshape não possui conta/
  servidor para recriá-los. Saldo local restante só pode reaparecer se o sistema
  restaurar dados locais, sem garantia. Apple ou Google decide e processa
  reembolsos e revogações. Sem conciliação oficial no servidor, o App pode não
  receber, detectar ou refletir a mudança prontamente ou nunca; dicas consumidas
  não podem ser recuperadas com confiança. Direitos irrenunciáveis do consumidor permanecem.</p>""",
    },
    "ru": {
        "privacy_intro": """<p>Настоящая Политика объясняет обработку информации при игре в
  <strong>Chesshape</strong> («Приложение»). <strong>Мы не запрашиваем имя,
  e-mail или учётную запись и не используем сервер для хранения игровых данных
  или покупок.</strong> Записи игры и выдачи хранятся локально; Google
  обрабатывает рекламные данные; платежи обрабатывает Apple App Store или Google Play.</p>""",
        "local_heading": "1. Локальные записи игры и покупок",
        "local_body": """<p>В закрытом локальном хранилище Приложение сохраняет:</p>
  <ul><li>прогресс, звёзды, рекорды, настройки, язык и доступность;</li>
  <li>остаток подсказок и серию ежедневных головоломок;</li>
  <li>право Premium и компактную отметку транзакции/выдачи против повторного начисления.</li></ul>
  <p>Полный чек магазина, данные карты и учётные данные магазина не сохраняются.
  Мы не видим эти локальные записи. В зависимости от настроек системы, учётной
  записи и устройства резервное копирование или перенос Apple/Google может их
  скопировать или восстановить. Удаление обычно стирает копию на устройстве, но
  не гарантирует удаление резервной копии платформы. Приложение не читает
  контакты, фото, файлы, точное местоположение или иной личный контент.</p>""",
        "payment_heading": "3. Покупки в Приложении и платёжные данные",
        "payment_body": """<p>Покупки обрабатывает <strong>Apple App Store</strong> на iOS и
  <strong>Google Play</strong> на Android по собственным условиям и политикам.
  Мы не получаем данные карты или платёжные реквизиты. Для выдачи и восстановления
  Premium нативный платёжный SDK временно передаёт Приложению чек либо токен
  покупки, идентификатор товара, статус, дату и ссылку транзакции. Эти значения
  не отправляются на сервер разработчика; сохраняется только компактный
  односторонний отпечаток выдачи из раздела 1. Возвраты и отзывы обрабатывает
  магазин. В этой
  клиентской версии нет авторитетной серверной сверки: Приложение узнает об
  изменении, только если магазин сообщит позже, и может не обнаружить или не
  отменить локальный Premium/контент вовремя либо вообще. Потраченные подсказки
  нельзя надёжно отозвать. Хранятся лишь право/остаток и компактная отметка из раздела 1.</p>""",
        "security_heading": "7. Безопасность, хранение и резервные копии",
        "security_body": """<p>Локальные записи игры и выдачи защищены песочницей ОС. Обычно они
  существуют, пока Приложение установлено, и могут попасть в резервную копию
  или перенос, контролируемые вами и платформой. Удаление обычно стирает локальную
  копию; резервная копия платформы может её восстановить. На сервере разработчика копий нет.</p>""",
        "terms_heading": "3. Покупки в Приложении",
        "terms_body": """<p>Через Apple App Store или Google Play по желанию предлагаются:</p>
  <ul><li><code>premium_no_ads</code> — нерасходуемая покупка, включающая Premium
  и убирающая рекламу. Первая подходящая исходная покупка даёт разовый бонус 25
  подсказок. Premium восстанавливается, но новое восстановление повторно бонус не выдаёт.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code> и
  <code>hints_100</code> — расходуемые наборы подсказок.</li></ul>
  <p><strong>Подписок нет.</strong> Магазин определяет и показывает до подтверждения
  итоговую локальную цену, валюту и налоги; действует цена магазина. Действуют и его условия.</p>
  <p>Premium восстанавливается с той же учётной записью магазина. Расходуемые
  наборы не восстанавливаются магазином между устройствами или переустановками;
  у Chesshape нет учётной записи/сервера для их воссоздания. Локальный остаток
  может вернуться лишь при восстановлении локальных данных ОС, что не гарантировано.
  Возвраты и отзывы решает и обрабатывает Apple или Google. Без авторитетной
  серверной сверки Приложение может не получить, не обнаружить или не отразить
  изменение вовремя либо вообще; потраченные подсказки нельзя надёжно отозвать.
  Неотчуждаемые права потребителя сохраняются.</p>""",
    },
    "id": {
        "privacy_intro": """<p>Kebijakan ini menjelaskan informasi yang ditangani saat memainkan
  <strong>Chesshape</strong> (“Aplikasi”). <strong>Kami tidak meminta nama,
  e-mail, atau akun dan tidak mengoperasikan server yang menyimpan data gim atau
  pembelian.</strong> Catatan gim dan pengiriman diproses lokal; Google memproses
  data iklan; Apple App Store atau Google Play memproses pembayaran seperti di bawah.</p>""",
        "local_heading": "1. Catatan gim dan pembelian lokal",
        "local_body": """<p>Aplikasi menyimpan di penyimpanan lokal privat:</p>
  <ul><li>progres, bintang, skor, pengaturan, bahasa, dan aksesibilitas;</li>
  <li>saldo petunjuk dan rangkaian teka-teki harian;</li>
  <li>hak Premium dan penanda transaksi/pengiriman ringkas untuk mencegah pemberian ganda.</li></ul>
  <p>Aplikasi tidak menyimpan tanda terima toko lengkap, data kartu, atau
  kredensial toko. Kami tidak dapat melihat catatan lokal ini. Bergantung pada
  pengaturan sistem, akun, dan perangkat, pencadangan atau transfer Apple/Google
  dapat menyalin atau memulihkannya. Menghapus instalasi biasanya menghapus
  salinan perangkat, tetapi tidak menjamin cadangan platform yang dapat dipulihkan
  ikut terhapus. Aplikasi tidak membaca kontak, foto, berkas, lokasi presisi, atau konten pribadi lain.</p>""",
        "payment_heading": "3. Pembelian dalam aplikasi dan data pembayaran",
        "payment_body": """<p>Pembelian diproses oleh <strong>Apple App Store</strong> di iOS dan
  <strong>Google Play</strong> di Android menurut ketentuan dan kebijakan mereka.
  Kami tidak menerima data kartu atau kredensial penagihan. Untuk pengiriman dan
  pemulihan Premium, SDK penagihan native memberikan sementara tanda terima atau
  token pembelian, ID produk, status, tanggal, dan referensi transaksi kepada
  Aplikasi. Nilai tersebut tidak dikirim ke server pengembang; hanya sidik jari
  pengiriman satu arah yang ringkas pada Bagian 1 yang disimpan. Toko menangani
  pengembalian dana/pencabutan.
  Versi khusus klien ini tidak memiliki rekonsiliasi server yang berwenang:
  Aplikasi hanya mengetahui perubahan jika toko melaporkannya kemudian dan
  mungkin tidak mendeteksi atau mencabut Premium/konten lokal dengan segera atau
  sama sekali. Petunjuk yang telah dipakai tidak dapat ditarik kembali secara
  andal. Aplikasi hanya menyimpan hak/saldo dan penanda ringkas pada Bagian 1.</p>""",
        "security_heading": "7. Keamanan, retensi, dan pencadangan",
        "security_body": """<p>Sandbox sistem melindungi catatan gim dan pengiriman lokal. Catatan
  biasanya ada selama Aplikasi terpasang dan dapat masuk ke cadangan atau
  transfer yang dikontrol Anda dan platform. Menghapus instalasi biasanya
  menghapus salinan lokal; cadangan platform dapat memulihkannya. Kami tidak
  menyimpan salinan di server pengembang.</p>""",
        "terms_heading": "3. Pembelian dalam aplikasi",
        "terms_body": """<p>Aplikasi menawarkan secara opsional melalui Apple App Store atau Google Play:</p>
  <ul><li><code>premium_no_ads</code> adalah pembelian non-konsumsi yang mengaktifkan
  Premium dan menghapus iklan. Pembelian asli pertama yang memenuhi syarat
  mencakup bonus satu kali 25 petunjuk. Premium dapat dipulihkan, tetapi pemulihan
  baru tidak memberikan bonus lagi.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code>, dan
  <code>hints_100</code> adalah paket petunjuk konsumsi.</li></ul>
  <p><strong>Tidak ada langganan.</strong> Toko mengontrol dan menampilkan sebelum
  konfirmasi harga lokal akhir, mata uang, dan pajak; harga toko berlaku. Ketentuan toko juga berlaku.</p>
  <p>Premium dapat dipulihkan dengan akun toko yang sama. Toko tidak memulihkan
  paket yang telah dikonsumsi antarperangkat atau instalasi ulang, dan Chesshape
  tidak memiliki akun/server untuk membuatnya kembali. Sisa saldo lokal mungkin
  kembali hanya jika sistem memulihkan data lokal, tanpa jaminan. Apple atau
  Google memutuskan dan memproses pengembalian dana/pencabutan. Tanpa rekonsiliasi
  server yang berwenang, Aplikasi mungkin tidak menerima, mendeteksi, atau
  mencerminkan perubahan dengan segera atau sama sekali; petunjuk terpakai tidak
  dapat ditarik kembali secara andal. Hak konsumen yang tidak dapat dikesampingkan tetap berlaku.</p>""",
    },
    "ja": {
        "privacy_intro": """<p>本ポリシーは <strong>Chesshape</strong>（以下「本アプリ」）で扱う情報を
  説明します。<strong>氏名、メール、アカウントを求めず、ゲームまたは購入記録を保存する
  サーバーも運用しません。</strong> ゲームと付与記録は端末内で処理され、広告データは
  Google、支払いは下記のとおり Apple App Store または Google Play が処理します。</p>""",
        "local_heading": "1. ゲームと購入に関するローカル記録",
        "local_body": """<p>本アプリのプライベートなローカル領域には次を保存します。</p>
  <ul><li>進行状況、スター、スコア、設定、言語、アクセシビリティ</li>
  <li>ヒント残数、デイリーパズルの連続記録</li>
  <li>Premium 権利と二重付与を防ぐコンパクトな取引・付与マーカー</li></ul>
  <p>ストアの完全なレシート、カード情報、ストア認証情報は保存しません。これらの
  ローカル記録を当方は参照できません。OS、アカウント、端末の設定により、Apple / Google
  のバックアップまたは端末移行でコピー・復元される場合があります。アンインストールは
  通常端末上のコピーを削除しますが、後で復元できるプラットフォームのバックアップまで
  削除される保証はありません。連絡先、写真、ファイル、正確な位置情報などは読み取りません。</p>""",
        "payment_heading": "3. アプリ内購入と支払いデータ",
        "payment_body": """<p>購入は iOS では <strong>Apple App Store</strong>、Android では
  <strong>Google Play</strong> が各規約・ポリシーに基づいて処理します。当方はカード情報や
  支払い認証情報を受け取りません。商品付与と Premium 復元のため、ネイティブ課金 SDK はレシート
  または購入トークン、商品 ID、状態、日付、取引参照を一時的に本アプリへ渡します。これらは
  開発者サーバーへ送信されず、第1項のコンパクトな一方向の付与フィンガープリントだけを保存します。
  返金・取消はストアが処理します。このクライアントのみの
  バージョンには権威あるサーバー照合がないため、ストアが後で通知した場合だけ変更を知り、ローカルの
  Premium／コンテンツを速やかに、または一切検出・取消できない場合があります。消費済みヒントを
  確実に回収することはできません。本アプリが保存するのは第1項の権利・残数とコンパクトなマーカーのみです。</p>""",
        "security_heading": "7. セキュリティ、保持、バックアップ",
        "security_body": """<p>ローカルのゲーム・付与記録は OS のアプリサンドボックスで保護されます。通常は
  インストール中保持され、お客様とプラットフォームが管理する OS バックアップや端末移行に
  含まれる場合があります。アンインストールで通常ローカルコピーは消えますが、プラットフォームの
  バックアップから復元されることがあります。開発者運用サーバーにコピーは保持しません。</p>""",
        "terms_heading": "3. アプリ内購入",
        "terms_body": """<p>Apple App Store または Google Play を通じて任意で次を提供します。</p>
  <ul><li><code>premium_no_ads</code> は Premium を有効にして広告をなくす非消耗型商品です。
  対象となる最初の新規購入には1回限り25ヒントが付きます。Premium は復元できますが、
  新しい環境での復元時にこのボーナスは再付与されません。</li>
  <li><code>hints_3</code>、<code>hints_10</code>、<code>hints_50</code>、
  <code>hints_100</code> は消耗型ヒントパックです。</li></ul>
  <p><strong>サブスクリプションはありません。</strong> 最終的な現地価格、通貨、税は確認前に
  ストアが表示・決定し、その価格が適用されます。ストアの規約も適用されます。</p>
  <p>Premium は同じストアアカウントで復元できます。消費済みヒントパックは端末間・再インストール時に
  ストアから復元されず、Chesshape に再作成するアカウント／サーバーはありません。残ったローカル残数は
  OS がローカルデータを復元した場合に限り戻ることがあり、保証されません。返金・取消は Apple または
  Google が判断・処理します。権威あるサーバー照合がないため、本アプリは変更を速やかに、または一切
  受信・検出・反映できない場合があり、消費済みヒントを確実に回収することはできません。放棄できない消費者の権利は制限されません。</p>""",
    },
    "ko": {
        "privacy_intro": """<p>본 방침은 <strong>Chesshape</strong>(이하 “앱”)에서 처리하는 정보를
  설명합니다. <strong>이름, 이메일, 계정을 요구하지 않으며 게임 또는 구매 기록을 저장하는
  서버도 운영하지 않습니다.</strong> 게임 및 지급 기록은 기기에서 처리되고, 광고 데이터는
  Google, 결제는 아래와 같이 Apple App Store 또는 Google Play가 처리합니다.</p>""",
        "local_heading": "1. 로컬 게임 및 구매 기록",
        "local_body": """<p>앱의 비공개 로컬 저장소에는 다음이 저장됩니다.</p>
  <ul><li>진행도, 별, 점수, 설정, 언어, 접근성</li>
  <li>힌트 잔액 및 일일 퍼즐 연속 기록</li>
  <li>Premium 권리와 중복 지급 방지용 간단한 거래·지급 표시</li></ul>
  <p>전체 스토어 영수증, 결제 카드 정보 또는 스토어 인증 정보는 저장하지 않습니다.
  저희는 이 로컬 기록을 볼 수 없습니다. OS, 계정 및 기기 설정에 따라 Apple/Google
  백업이나 기기 이전으로 복사 또는 복원될 수 있습니다. 앱 삭제 시 일반적으로 기기
  사본은 지워지지만 나중에 복원 가능한 플랫폼 백업의 삭제까지 보장되지는 않습니다.
  연락처, 사진, 파일, 정확한 위치 또는 기타 개인 콘텐츠를 읽지 않습니다.</p>""",
        "payment_heading": "3. 인앱 구매 및 결제 데이터",
        "payment_body": """<p>구매는 iOS에서 <strong>Apple App Store</strong>, Android에서
  <strong>Google Play</strong>가 자체 약관과 정책에 따라 처리합니다. 저희는 카드 정보나
  결제 인증 정보를 받지 않습니다. 상품 지급과 Premium 복원을 위해 네이티브 결제 SDK는
  영수증 또는 구매 토큰, 상품 ID, 구매 상태, 날짜 및 거래 참조를 앱에 일시적으로 제공합니다.
  이 값은 개발자 서버로 전송되지 않으며 제1항의 간단한 단방향 지급 지문만 저장됩니다. 환불·취소는 스토어가
  처리합니다. 이 클라이언트 전용 버전에는 권한 있는 서버 대사가 없어 스토어가 나중에 알린
  경우에만 변경을 알 수 있고 로컬 Premium/콘텐츠를 제때 또는 전혀 감지·취소하지 못할 수
  있습니다. 사용한 힌트는 안정적으로 회수할 수 없습니다. 앱은 제1항의 권리/잔액과 간단한 표시만 저장합니다.</p>""",
        "security_heading": "7. 보안, 보관 및 백업",
        "security_body": """<p>로컬 게임 및 지급 기록은 OS 앱 샌드박스로 보호됩니다. 일반적으로 앱 설치 중
  유지되며 사용자와 플랫폼이 관리하는 OS 백업이나 기기 이전에 포함될 수 있습니다.
  앱 삭제 시 보통 로컬 사본은 지워지지만 플랫폼 백업에서 나중에 복원될 수 있습니다.
  개발자 운영 서버에는 사본을 보관하지 않습니다.</p>""",
        "terms_heading": "3. 인앱 구매",
        "terms_body": """<p>Apple App Store 또는 Google Play를 통해 다음 선택 상품을 제공합니다.</p>
  <ul><li><code>premium_no_ads</code>는 Premium을 활성화하고 광고를 제거하는 비소모성
  상품입니다. 자격을 갖춘 최초 신규 구매에는 1회 25개 힌트 보너스가 포함됩니다.
  Premium은 복원되지만 새 환경에서 복원할 때 이 보너스가 다시 지급되지는 않습니다.</li>
  <li><code>hints_3</code>, <code>hints_10</code>, <code>hints_50</code>,
  <code>hints_100</code>은 소모성 힌트 팩입니다.</li></ul>
  <p><strong>구독은 없습니다.</strong> 최종 현지 가격, 통화 및 세금은 확인 전에 스토어가
  표시하고 결정하며 스토어 가격이 적용됩니다. 해당 스토어 약관도 적용됩니다.</p>
  <p>Premium은 같은 스토어 계정으로 복원할 수 있습니다. 소비된 힌트 팩은 기기 간 또는
  재설치 시 스토어가 복원하지 않으며 Chesshape에는 이를 재생성할 계정/서버가 없습니다.
  남은 로컬 잔액은 OS가 로컬 데이터를 복원한 경우에만 돌아올 수 있고 보장되지 않습니다.
  환불 및 취소는 Apple 또는 Google이 결정·처리합니다. 권한 있는 서버 대사가 없어 앱은
  변경을 제때 또는 전혀 수신·감지·반영하지 못할 수 있고, 사용한 힌트는 안정적으로 회수할
  수 없습니다. 포기할 수 없는 소비자 권리는 제한되지 않습니다.</p>""",
    },
}


# These short disclosures are kept separately from the longer editorial blocks
# above so the release-critical purchase lifecycle facts can be asserted with
# exact locale parity. They are appended at the normalization boundary below.
_IAP_FINAL_DISCLOSURES = {
    "en": {
        "local_intent": """<p>If a Premium purchase remains unresolved or is
  interrupted, the App also keeps a local purchase-intent marker containing the
  product identifier, an app-generated attempt identifier and the purchase start
  time. It is used only to resume or reconcile that attempt with the store and is
  removed after a terminal result or when the 30-day reconciliation window
  expires.</p>""",
        "store_privacy": """<p>Apple and Google process their store and payment
  data under their own privacy policies: <a href="https://www.apple.com/legal/privacy/"
  rel="noopener">Apple Privacy Policy</a> and <a href="https://policies.google.com/privacy"
  rel="noopener">Google Privacy Policy</a>.</p>""",
        "pending": """<p>A pending or interrupted purchase is not delivered until
  the applicable store reports it as completed.</p>""",
        "cross_platform": """<p>Premium may be restored only with the same store
  account on the platform where it was purchased. Apple App Store and Google Play
  entitlements are separate; a purchase made through one cannot be restored
  through the other.</p>""",
    },
    "tr": {
        "local_intent": """<p>Premium satın alma işlemi sonuçlanmamış veya kesintiye
  uğramışsa Uygulama ayrıca ürün kimliğini, Uygulamanın oluşturduğu deneme kimliğini
  ve satın almanın başlangıç zamanını içeren yerel bir satın alma niyet işareti
  tutar. Bu işaret yalnızca ilgili denemeyi sürdürmek veya mağaza kaydıyla
  uzlaştırmak için kullanılır; kesin sonuç alındığında veya 30 günlük uzlaştırma
  süresi dolduğunda silinir.</p>""",
        "store_privacy": """<p>Apple ve Google, mağaza ve ödeme verilerini kendi
  gizlilik politikalarına göre işler: <a href="https://www.apple.com/legal/privacy/"
  rel="noopener">Apple Gizlilik Politikası</a> ve
  <a href="https://policies.google.com/privacy" rel="noopener">Google Gizlilik
  Politikası</a>.</p>""",
        "pending": """<p>Bekleyen veya kesintiye uğrayan satın alma, ilgili mağaza
  işlemin tamamlandığını bildirene kadar teslim edilmez.</p>""",
        "cross_platform": """<p>Premium yalnızca satın alındığı platformdaki aynı
  mağaza hesabıyla geri yüklenebilir. Apple App Store ve Google Play hakları
  ayrıdır; birinden alınan ürün diğerinde geri yüklenemez.</p>""",
    },
    "de": {
        "local_intent": """<p>Bleibt ein Premium-Kauf ungeklärt oder wird er
  unterbrochen, speichert die App außerdem lokal eine Kaufabsichtsmarke mit
  Produktkennung, einer von der App erzeugten Versuchskennung und Startzeit des
  Kaufs. Sie dient nur dazu, diesen Versuch fortzusetzen oder mit dem Store
  abzugleichen, und wird nach einem endgültigen Ergebnis oder nach Ablauf des
  30-tägigen Abgleichszeitraums gelöscht.</p>""",
        "store_privacy": """<p>Apple und Google verarbeiten ihre Store- und
  Zahlungsdaten nach ihren eigenen Datenschutzrichtlinien:
  <a href="https://www.apple.com/legal/privacy/" rel="noopener">Apple-
  Datenschutzrichtlinie</a> und <a href="https://policies.google.com/privacy"
  rel="noopener">Google-Datenschutzrichtlinie</a>.</p>""",
        "pending": """<p>Ein ausstehender oder unterbrochener Kauf wird erst
  ausgeliefert, wenn der jeweilige Store ihn als abgeschlossen meldet.</p>""",
        "cross_platform": """<p>Premium kann nur mit demselben Store-Konto auf
  der Plattform des Kaufs wiederhergestellt werden. Berechtigungen des Apple App
  Store und von Google Play sind getrennt; ein Kauf aus dem einen Store kann im
  anderen nicht wiederhergestellt werden.</p>""",
    },
    "es": {
        "local_intent": """<p>Si una compra de Premium queda sin resolver o se
  interrumpe, la App también conserva localmente una marca de intención de compra
  con el identificador del producto, un identificador de intento generado por la
  App y la hora de inicio de la compra. Solo se usa para reanudar o conciliar ese
  intento con la tienda y se elimina tras un resultado definitivo o al vencer
  el periodo de conciliación de 30 días.</p>""",
        "store_privacy": """<p>Apple y Google tratan sus datos de tienda y pago
  conforme a sus propias políticas de privacidad: la
  <a href="https://www.apple.com/legal/privacy/" rel="noopener">Política de
  Privacidad de Apple</a> y la <a href="https://policies.google.com/privacy"
  rel="noopener">Política de Privacidad de Google</a>.</p>""",
        "pending": """<p>Una compra pendiente o interrumpida no se entrega hasta
  que la tienda correspondiente informa de que se ha completado.</p>""",
        "cross_platform": """<p>Premium solo puede restaurarse con la misma cuenta
  de tienda en la plataforma donde se compró. Los derechos de Apple App Store y
  Google Play son independientes; una compra realizada en uno no puede
  restaurarse en el otro.</p>""",
    },
    "fr": {
        "local_intent": """<p>Si un achat Premium reste non résolu ou est
  interrompu, l'App conserve aussi localement un marqueur d'intention d'achat
  contenant l'identifiant du produit, un identifiant de tentative généré par
  l'App et l'heure de début de l'achat. Il sert uniquement à reprendre ou à
  rapprocher cette tentative avec le store et est supprimé après un résultat
  définitif ou à l'expiration du délai de rapprochement de 30 jours.</p>""",
        "store_privacy": """<p>Apple et Google traitent leurs données de store et
  de paiement selon leurs propres politiques de confidentialité : la
  <a href="https://www.apple.com/legal/privacy/" rel="noopener">Politique de
  confidentialité d'Apple</a> et la <a href="https://policies.google.com/privacy"
  rel="noopener">Politique de confidentialité de Google</a>.</p>""",
        "pending": """<p>Un achat en attente ou interrompu n'est pas livré tant
  que le store concerné ne l'a pas déclaré terminé.</p>""",
        "cross_platform": """<p>Premium ne peut être restauré qu'avec le même
  compte de store sur la plateforme où il a été acheté. Les droits Apple App
  Store et Google Play sont distincts : un achat effectué sur l'un ne peut pas
  être restauré sur l'autre.</p>""",
    },
    "it": {
        "local_intent": """<p>Se un acquisto Premium resta irrisolto o viene
  interrotto, l'App conserva inoltre in locale un indicatore di intenzione di
  acquisto contenente l'identificativo del prodotto, un identificativo del
  tentativo generato dall'App e l'ora di inizio dell'acquisto. Serve solo a
  riprendere o riconciliare quel tentativo con lo store e viene eliminato dopo
  un esito definitivo o alla scadenza del periodo di riconciliazione di 30
  giorni.</p>""",
        "store_privacy": """<p>Apple e Google trattano i dati dello store e di
  pagamento secondo le rispettive informative sulla privacy:
  <a href="https://www.apple.com/legal/privacy/" rel="noopener">Informativa sulla
  privacy di Apple</a> e <a href="https://policies.google.com/privacy"
  rel="noopener">Norme sulla privacy di Google</a>.</p>""",
        "pending": """<p>Un acquisto in sospeso o interrotto non viene consegnato
  finché lo store interessato non lo segnala come completato.</p>""",
        "cross_platform": """<p>Premium può essere ripristinato solo con lo stesso
  account dello store sulla piattaforma in cui è stato acquistato. I diritti di
  Apple App Store e Google Play sono separati: un acquisto effettuato su uno non
  può essere ripristinato sull'altro.</p>""",
    },
    "pt": {
        "local_intent": """<p>Se uma compra Premium permanecer sem solução ou for
  interrompida, o App também mantém localmente um marcador de intenção de compra
  com o identificador do produto, um identificador de tentativa gerado pelo App
  e o horário de início da compra. Ele é usado apenas para retomar ou conciliar
  essa tentativa com a loja e é removido após um resultado definitivo ou ao
  fim do período de conciliação de 30 dias.</p>""",
        "store_privacy": """<p>Apple e Google tratam seus dados de loja e pagamento
  conforme suas próprias políticas de privacidade: a
  <a href="https://www.apple.com/legal/privacy/" rel="noopener">Política de
  Privacidade da Apple</a> e a <a href="https://policies.google.com/privacy"
  rel="noopener">Política de Privacidade do Google</a>.</p>""",
        "pending": """<p>Uma compra pendente ou interrompida não é entregue até
  que a loja correspondente informe que ela foi concluída.</p>""",
        "cross_platform": """<p>Premium só pode ser restaurado com a mesma conta
  da loja na plataforma em que foi comprado. Os direitos da Apple App Store e do
  Google Play são separados; uma compra feita em uma loja não pode ser restaurada
  na outra.</p>""",
    },
    "ru": {
        "local_intent": """<p>Если покупка Premium остаётся незавершённой или
  прерывается, Приложение также локально хранит отметку о намерении покупки:
  идентификатор товара, созданный Приложением идентификатор попытки и время
  начала покупки. Она используется только для продолжения или сверки этой
  попытки с магазином и удаляется после окончательного результата либо по
  истечении 30-дневного срока сверки.</p>""",
        "store_privacy": """<p>Apple и Google обрабатывают данные магазина и
  платежей согласно собственным политикам конфиденциальности:
  <a href="https://www.apple.com/legal/privacy/" rel="noopener">Политике
  конфиденциальности Apple</a> и <a href="https://policies.google.com/privacy"
  rel="noopener">Политике конфиденциальности Google</a>.</p>""",
        "pending": """<p>Ожидающая или прерванная покупка не выдаётся, пока
  соответствующий магазин не сообщит о её завершении.</p>""",
        "cross_platform": """<p>Premium можно восстановить только с той же учётной
  записью магазина на платформе покупки. Права Apple App Store и Google Play
  раздельны: покупку из одного магазина нельзя восстановить в другом.</p>""",
    },
    "id": {
        "local_intent": """<p>Jika pembelian Premium belum terselesaikan atau
  terputus, Aplikasi juga menyimpan secara lokal penanda niat pembelian yang
  berisi pengenal produk, pengenal upaya yang dibuat Aplikasi, dan waktu mulai
  pembelian. Penanda ini hanya digunakan untuk melanjutkan atau merekonsiliasi
  upaya tersebut dengan toko dan dihapus setelah hasil akhir diperoleh atau
  setelah masa rekonsiliasi 30 hari berakhir.</p>""",
        "store_privacy": """<p>Apple dan Google memproses data toko dan pembayaran
  mereka menurut kebijakan privasi masing-masing:
  <a href="https://www.apple.com/legal/privacy/" rel="noopener">Kebijakan Privasi
  Apple</a> dan <a href="https://policies.google.com/privacy" rel="noopener">Kebijakan
  Privasi Google</a>.</p>""",
        "pending": """<p>Pembelian yang tertunda atau terputus tidak diberikan
  sampai toko terkait melaporkannya sebagai selesai.</p>""",
        "cross_platform": """<p>Premium hanya dapat dipulihkan dengan akun toko
  yang sama pada platform tempat pembelian dilakukan. Hak Apple App Store dan
  Google Play terpisah; pembelian melalui salah satunya tidak dapat dipulihkan
  melalui yang lain.</p>""",
    },
    "ja": {
        "local_intent": """<p>Premium の購入が未解決または中断された場合、本アプリは商品 ID、
  本アプリが生成した試行 ID、購入開始時刻を含む購入意図マーカーも端末内に保存します。
  このマーカーは、その試行を再開またはストアと照合するためだけに使用し、最終結果が
  確定した時点、または30日間の照合期間が満了した時点で削除します。</p>""",
        "store_privacy": """<p>Apple と Google は、各社のプライバシーポリシーに基づき
  ストアおよび支払いデータを処理します：<a href="https://www.apple.com/legal/privacy/"
  rel="noopener">Apple プライバシーポリシー</a>、<a href="https://policies.google.com/privacy"
  rel="noopener">Google プライバシーポリシー</a>。</p>""",
        "pending": """<p>保留中または中断された購入は、該当ストアが完了と報告するまで
  商品を付与しません。</p>""",
        "cross_platform": """<p>Premium を復元できるのは、購入したプラットフォームの
  同じストアアカウントに限られます。Apple App Store と Google Play の権利は別々であり、
  一方で行った購入を他方で復元することはできません。</p>""",
    },
    "ko": {
        "local_intent": """<p>Premium 구매가 해결되지 않았거나 중단된 경우 앱은 상품 ID,
  앱이 생성한 시도 ID 및 구매 시작 시간이 포함된 구매 의도 표시도 로컬에 저장합니다.
  이 표시는 해당 시도를 재개하거나 스토어와 대조하는 데만 사용되며 최종 결과가 확정되거나
  30일의 대조 기간이 만료되면 삭제됩니다.</p>""",
        "store_privacy": """<p>Apple과 Google은 각자의 개인정보처리방침에 따라 스토어 및
  결제 데이터를 처리합니다: <a href="https://www.apple.com/legal/privacy/"
  rel="noopener">Apple 개인정보 처리방침</a> 및
  <a href="https://policies.google.com/privacy" rel="noopener">Google 개인정보 처리방침</a>.</p>""",
        "pending": """<p>보류 중이거나 중단된 구매는 해당 스토어가 완료되었다고 보고할
  때까지 지급되지 않습니다.</p>""",
        "cross_platform": """<p>Premium은 구매한 플랫폼의 동일한 스토어 계정으로만 복원할
  수 있습니다. Apple App Store와 Google Play의 권리는 서로 분리되어 있으므로 한쪽에서 한
  구매를 다른 쪽에서 복원할 수 없습니다.</p>""",
    },
}


_TELEMETRY_COPY = {
    "en": ("4. Analytics and crash diagnostics", """<p>The App package includes the
  <strong>Firebase Analytics</strong> and <strong>Firebase Crashlytics</strong>
  software libraries. In this release, collection for both is explicitly
  disabled in the native platform configuration and again at App startup.
  Gameplay events use a no-operation logger. Accordingly, the App does not send
  analytics events or crash reports to Firebase or to us through those libraries
  in this release. There are no accounts, name/e-mail collection, or developer-
  operated database holding your data. If telemetry is enabled in a future
  release, this policy and its effective date will be updated before release.</p>"""),
    "tr": ("4. Analitik ve çökme tanılama", """<p>Uygulama paketinde
  <strong>Firebase Analytics</strong> ve <strong>Firebase Crashlytics</strong>
  yazılım kütüphaneleri bulunur. Bu sürümde her ikisinin veri toplaması hem yerel
  platform ayarlarında hem Uygulama başlangıcında açıkça kapatılmıştır. Oyun
  olayları hiçbir işlem yapmayan bir kaydediciye bağlıdır. Dolayısıyla bu sürümde
  bu kütüphaneler üzerinden Firebase'e veya bize analitik olayı ya da çökme raporu
  gönderilmez. Hesap, ad/e-posta toplama veya verilerinizi tutan geliştirici
  veritabanı yoktur. Telemetri ileride açılırsa bu politika ve yürürlük tarihi
  sürüm yayımlanmadan önce güncellenecektir.</p>"""),
    "de": ("4. Analyse und Absturzdiagnose", """<p>Das App-Paket enthält die
  Bibliotheken <strong>Firebase Analytics</strong> und <strong>Firebase
  Crashlytics</strong>. In dieser Version ist die Erfassung für beide sowohl in
  der nativen Plattformkonfiguration als auch beim App-Start ausdrücklich
  deaktiviert. Spielereignisse nutzen einen inaktiven Logger. Daher sendet die
  App in dieser Version über diese Bibliotheken keine Analyseereignisse oder
  Absturzberichte an Firebase oder uns. Es gibt keine Konten, Namens-/E-Mail-
  Erfassung oder Entwicklerdatenbank mit Ihren Daten. Wird Telemetrie künftig
  aktiviert, aktualisieren wir Richtlinie und Datum vor der Veröffentlichung.</p>"""),
    "es": ("4. Analítica y diagnóstico de fallos", """<p>El paquete incluye las
  bibliotecas <strong>Firebase Analytics</strong> y <strong>Firebase
  Crashlytics</strong>. En esta versión, la recogida de ambas está desactivada
  expresamente en la configuración nativa y de nuevo al iniciar la App. Los
  eventos de juego usan un registrador inactivo. Por tanto, estas bibliotecas no
  envían eventos analíticos ni informes de fallos a Firebase o a nosotros en
  esta versión. No hay cuentas, recogida de nombre/correo ni base de datos del
  desarrollador con tus datos. Si se activa telemetría en el futuro, se
  actualizarán esta política y la fecha antes de publicar.</p>"""),
    "fr": ("4. Analyse et diagnostic des plantages", """<p>Le paquet contient
  les bibliothèques <strong>Firebase Analytics</strong> et <strong>Firebase
  Crashlytics</strong>. Dans cette version, leur collecte est expressément
  désactivée dans la configuration native puis au démarrage de l'App. Les
  événements de jeu utilisent un enregistreur inactif. Ces bibliothèques
  n'envoient donc aucun événement analytique ni rapport de plantage à Firebase
  ou à nous dans cette version. Il n'existe ni compte, ni collecte de nom/e-mail,
  ni base du développeur contenant vos données. Toute activation future de la
  télémétrie entraînera la mise à jour de cette politique et de sa date avant publication.</p>"""),
    "it": ("4. Analisi e diagnostica degli arresti", """<p>Il pacchetto include
  le librerie <strong>Firebase Analytics</strong> e <strong>Firebase
  Crashlytics</strong>. In questa versione la raccolta di entrambe è
  esplicitamente disattivata nella configurazione nativa e di nuovo all'avvio
  dell'App. Gli eventi di gioco usano un logger inattivo. Pertanto in questa
  versione tali librerie non inviano eventi analitici o rapporti di arresto a
  Firebase o a noi. Non esistono account, raccolta di nome/e-mail o database
  dello sviluppatore con i tuoi dati. Se in futuro la telemetria sarà attivata,
  informativa e data saranno aggiornate prima della pubblicazione.</p>"""),
    "pt": ("4. Análise e diagnóstico de falhas", """<p>O pacote inclui as
  bibliotecas <strong>Firebase Analytics</strong> e <strong>Firebase
  Crashlytics</strong>. Nesta versão, a coleta de ambas está expressamente
  desativada na configuração nativa e novamente ao iniciar o App. Eventos do
  jogo usam um registrador inativo. Assim, nesta versão essas bibliotecas não
  enviam eventos analíticos ou relatórios de falha ao Firebase ou a nós. Não há
  contas, coleta de nome/e-mail nem banco do desenvolvedor com seus dados. Se a
  telemetria for ativada futuramente, esta política e a data serão atualizadas antes da publicação.</p>"""),
    "ru": ("4. Аналитика и диагностика сбоев", """<p>Пакет содержит библиотеки
  <strong>Firebase Analytics</strong> и <strong>Firebase Crashlytics</strong>.
  В этой версии сбор обеими библиотеками явно отключён в нативных настройках и
  повторно при запуске Приложения. Игровые события направлены в неактивный
  регистратор. Поэтому в этой версии аналитические события и отчёты о сбоях
  через эти библиотеки не отправляются в Firebase или нам. Нет учётных записей,
  сбора имени/e-mail или базы разработчика с вашими данными. При будущем
  включении телеметрии политика и дата будут обновлены до публикации.</p>"""),
    "id": ("4. Analitik dan diagnostik kerusakan", """<p>Paket Aplikasi memuat
  pustaka <strong>Firebase Analytics</strong> dan <strong>Firebase
  Crashlytics</strong>. Dalam rilis ini, pengumpulan keduanya dinonaktifkan
  secara tegas di konfigurasi platform native dan kembali saat Aplikasi mulai.
  Peristiwa gim memakai pencatat tanpa operasi. Karena itu, pustaka tersebut
  tidak mengirim peristiwa analitik atau laporan kerusakan ke Firebase atau kami
  dalam rilis ini. Tidak ada akun, pengumpulan nama/e-mail, atau basis data
  pengembang yang menyimpan data Anda. Jika telemetri diaktifkan kelak, kebijakan
  dan tanggal ini akan diperbarui sebelum rilis.</p>"""),
    "ja": ("4. 解析とクラッシュ診断", """<p>本アプリのパッケージには
  <strong>Firebase Analytics</strong> と <strong>Firebase Crashlytics</strong> の
  ライブラリが含まれます。ただし本バージョンでは、両方の収集をネイティブ設定および
  アプリ起動時に明示的に無効化しています。ゲームイベントは何も送らないロガーを使用します。
  したがって本バージョンでは、これらを通じて解析イベントやクラッシュレポートを Firebase
  または当方へ送信しません。アカウント、氏名・メールの収集、データを保持する開発者データ
  ベースもありません。将来テレメトリを有効化する場合は、公開前に本ポリシーと発効日を更新します。</p>"""),
    "ko": ("4. 분석 및 충돌 진단", """<p>앱 패키지에는 <strong>Firebase
  Analytics</strong>와 <strong>Firebase Crashlytics</strong> 라이브러리가 포함됩니다.
  하지만 이 버전에서는 두 라이브러리의 수집을 네이티브 플랫폼 설정과 앱 시작 시점에
  명시적으로 비활성화합니다. 게임 이벤트는 아무 작업도 하지 않는 로거를 사용합니다.
  따라서 이 버전에서는 이 라이브러리를 통해 Firebase 또는 저희에게 분석 이벤트나 충돌
  보고서를 보내지 않습니다. 계정, 이름/이메일 수집 또는 사용자 데이터를 보관하는 개발자
  데이터베이스도 없습니다. 향후 원격 측정을 활성화하면 출시 전에 본 방침과 발효일을 갱신합니다.</p>"""),
}


_IAP_SUPPORT = {
    "en": "For purchase delivery or restore help, contact",
    "tr": "Satın alma teslimi veya geri yükleme desteği için yazın:",
    "de": "Hilfe bei Kauf-Auslieferung oder Wiederherstellung erhalten Sie unter",
    "es": "Para ayuda con la entrega o restauración de una compra, escribe a",
    "fr": "Pour toute aide de livraison ou restauration d'un achat, contactez",
    "it": "Per assistenza su consegna o ripristino di un acquisto, scrivi a",
    "pt": "Para ajuda com entrega ou restauração de uma compra, contate",
    "ru": "По вопросам выдачи или восстановления покупки пишите на",
    "id": "Untuk bantuan pengiriman atau pemulihan pembelian, hubungi",
    "ja": "購入の付与または復元に関するサポート:",
    "ko": "구매 지급 또는 복원 지원 문의:",
}


def _renumber(heading, number):
    """Keep the localized title while assigning the shared section number."""
    _, separator, title = heading.partition(". ")
    return f"{number}. {title if separator else heading}"


for _code, _lang_data in LANGS.items():
    _copy = _PURCHASE_COPY[_code]
    _final_iap = _IAP_FINAL_DISCLOSURES[_code]
    _lang_data["privacy"]["intro"] = _copy["privacy_intro"]

    _old_privacy = _lang_data["privacy"]["sections"]
    _lang_data["privacy"]["sections"] = [
        (_copy["local_heading"],
         f'{_copy["local_body"]}\n  {_final_iap["local_intent"]}'),
        (_renumber(_old_privacy[1][0], 2), _old_privacy[1][1]),
        (_copy["payment_heading"],
         f'{_copy["payment_body"]}\n  {_final_iap["store_privacy"]}'),
        _TELEMETRY_COPY[_code],
        (_renumber(_old_privacy[3][0], 5), _old_privacy[3][1]),
        (_renumber(_old_privacy[4][0], 6), _old_privacy[4][1]),
        (_copy["security_heading"], _copy["security_body"]),
        (_renumber(_old_privacy[6][0], 8), _old_privacy[6][1]),
    ]

    _old_terms = _lang_data["terms"]["sections"]
    _lang_data["terms"]["sections"] = [
        (_renumber(_old_terms[0][0], 1), _old_terms[0][1]),
        (_renumber(_old_terms[1][0], 2), _old_terms[1][1]),
        (_copy["terms_heading"],
         f'{_copy["terms_body"]}\n  {_final_iap["pending"]}\n'
         f'  {_final_iap["cross_platform"]}\n'
         f'  <p>{_IAP_SUPPORT[_code]} '
         f'<a href="mailto:{CONTACT}">{CONTACT}</a>.</p>'),
        *[(_renumber(heading, index + 1), body)
          for index, (heading, body) in enumerate(_old_terms[2:], start=3)],
    ]
