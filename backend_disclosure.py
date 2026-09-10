"""Android purchase data disclosure; shared facts across all existing legal locales."""

BACKEND_DISCLOSURE = {'en': {'overview': 'You can play without registering or signing in. Android uses an automatically '
                    'created technical user ID for the purchase checks described below.',
        'purchase': 'Apple and Google process payments; we do not receive your full payment-card '
                    'details. When Android purchase verification is enabled, Firebase '
                    'Authentication creates an automatic technical user ID without a registration '
                    'screen. App Check uses Play Integrity to protect the service. Checks may run '
                    'at startup, purchase or restore. Google processes authentication IP '
                    'addresses, technical device information and integrity tokens. The app sends '
                    'its user ID, Google Play purchase token and product details to our Google '
                    'Cloud/Firebase verification service over HTTPS. Our purchase ledger stores a '
                    'one-way hash of the purchase token instead of the raw token. It separately '
                    'records the technical user ID, product, transaction dates, region, delivery '
                    'status, purchased rights and refund status. These records validate purchases '
                    'and prevent fraud or duplicate rewards. External sites have their own privacy '
                    'policies.',
        'retention': 'Purchase verification records are kept to maintain purchased access and '
                     'prevent repeated rewards. Uninstalling does not delete these server records. '
                     'Contact the address below to request access or deletion; requests are '
                     'assessed under applicable privacy rights and necessary record retention. '
                     'Provider-held data is also subject to the relevant Google, Firebase and '
                     'store policies.',
        'security': 'Local data is protected by the operating system. Purchase verification and '
                    'Firebase requests use HTTPS. Device backups, store records and '
                    'service-provider data may remain after the app is uninstalled.',
        'local': 'Game progress, settings, hint balance, purchased access and delivery markers are '
                 'kept on your device. Depending on your device and backup settings, the operating '
                 'system may retain or restore a copy. The app does not read contacts, photos or '
                 'precise location. Limited Android purchase details are processed by the '
                 'verification service described below.',
        'analytics': 'Production releases use Firebase Analytics and Firebase Crashlytics for '
                     'feature usage and reliability. They process installation or session '
                     'identifiers, gameplay interactions, purchase and advertising outcomes, '
                     'technical app/device data and crash diagnostics. Analytics '
                     'advertising-identifier access and advertising-personalization signals are '
                     'disabled. Firebase Remote Config uses a Firebase installation identifier and '
                     'technical information to fetch an optional More Games catalog. These '
                     'services are distinct from Android purchase authentication and verification.',
        'chess_terms': 'Available products are shown with the price supplied by the store. '
                       'Consumable hint packs contain 10, 50 or 200 hints. Premium removes '
                       'automatic ads; optional rewarded ads remain available. Its first eligible '
                       'purchase includes 60 hints once; restoring Premium does not grant the '
                       'bonus again. Restore does not replenish spent hints. Apple and Google '
                       'handle payments and refunds. Android purchase verification checks '
                       'transaction and refund status through the service described in the Privacy '
                       'Policy; store and network availability can affect when changes are '
                       'reflected.'},
 'tr': {'overview': 'Oynamak için kayıt olmanız veya oturum açmanız gerekmez. Android satın alma '
                    'kontrollerinde, aşağıda açıklanan otomatik teknik kullanıcı kimliği '
                    'kullanılır.',
        'purchase': 'Ödemeleri Apple ve Google işler; ödeme kartınızın tüm bilgilerini almayız. '
                    'Android satın alma doğrulaması etkin olduğunda Firebase Authentication, kayıt '
                    'ekranı gerektirmeden otomatik bir teknik kullanıcı kimliği oluşturur. App '
                    'Check, hizmeti korumak için Play Integrity kullanır. Kontroller uygulama '
                    'açılırken, satın alma veya geri yükleme sırasında yapılabilir. Google, kimlik '
                    'doğrulama için IP adreslerini, teknik cihaz bilgilerini ve bütünlük doğrulama '
                    'belirteçlerini işler. Uygulama, kullanıcı kimliğini, Google Play satın alma '
                    'belirtecini ve ürün bilgilerini HTTPS üzerinden Google Cloud/Firebase '
                    'üzerindeki doğrulama hizmetimize gönderir. Satın alma kayıtlarında ham satın '
                    'alma belirteci yerine bunun tek yönlü özeti saklanır. Teknik kullanıcı '
                    'kimliği, ürün, işlem tarihleri, bölge, teslim durumu, satın alınan haklar ve '
                    'iade durumu ayrı alanlarda kaydedilir. Bu kayıtlar satın almaları doğrulamak, '
                    'dolandırıcılığı ve aynı ödülün tekrar verilmesini önlemek için kullanılır. '
                    'Harici sitelerin kendi gizlilik politikaları geçerlidir.',
        'retention': 'Satın alma doğrulama kayıtları, satın alınan hakları korumak ve aynı ödülün '
                     'tekrar verilmesini önlemek için saklanır. Uygulamayı kaldırmak bu sunucu '
                     'kayıtlarını silmez. Erişim veya silme talebi için aşağıdaki adrese '
                     'yazabilirsiniz; talepler geçerli gizlilik hakları ve kayıtların saklanma '
                     'gereksinimi çerçevesinde değerlendirilir. Hizmet sağlayıcılardaki veriler '
                     'ayrıca ilgili Google, Firebase ve mağaza politikalarına tabidir.',
        'security': 'Yerel veriler işletim sistemi tarafından korunmaktadır. Satın alma '
                    "doğrulaması ve Firebase istekleri HTTPS'yi kullanır. Uygulama kaldırıldıktan "
                    'sonra cihaz yedeklemeleri, mağaza kayıtları ve servis sağlayıcı verileri '
                    'kalabilir.',
        'local': 'Oyun ilerlemesi, ayarlar, ipucu bakiyesi, satın alınan erişim ve teslimat '
                 'işaretleri cihazınızda saklanır. Cihazınıza ve yedekleme ayarlarınıza bağlı '
                 'olarak işletim sistemi bir kopyayı saklayabilir veya geri yükleyebilir. Uygulama '
                 'kişileri, fotoğrafları veya kesin konumu okumaz. Sınırlı Android satın alma '
                 'ayrıntıları, aşağıda açıklanan doğrulama hizmeti tarafından işlenir.',
        'analytics': 'Yayımlanan sürümlerde özellik kullanımını ve güvenilirliği değerlendirmek '
                     'için Firebase Analytics ve Firebase Crashlytics kullanılır. Bu hizmetler '
                     'kurulum veya oturum kimliklerini, oyun etkileşimlerini, satın alma ve reklam '
                     'sonuçlarını, teknik uygulama/cihaz verilerini ve çökme tanılama bilgilerini '
                     'işler. Analytics için reklam kimliğine erişim ve reklam kişiselleştirme '
                     'sinyalleri kapalıdır. Firebase Remote Config, isteğe bağlı Diğer Oyunlar '
                     'kataloğunu almak için Firebase kurulum kimliğini ve teknik bilgileri '
                     'kullanır. Bu hizmetler Android satın alma kimlik doğrulaması ve ödeme '
                     'doğrulamasından ayrıdır.',
        'chess_terms': 'Mağazada sunulan ürünler, mağazanın bildirdiği fiyatla gösterilir. '
                       'Tüketilebilir ipucu paketleri 10, 50 veya 200 ipucu içerir. Premium '
                       'otomatik reklamları kaldırır; isteğe bağlı ödüllü reklamlar '
                       'kullanılabilir. İlk uygun Premium satın alımında bir kez 60 ipucu verilir; '
                       'Premium geri yüklendiğinde bu bonus yeniden verilmez. Geri yükleme, '
                       'harcanmış ipuçlarını yenilemez. Ödemeleri ve iadeleri Apple ve Google '
                       'yönetir. Android satın alma doğrulaması, Gizlilik Politikası’nda açıklanan '
                       'hizmet üzerinden işlem ve iade durumunu kontrol eder; değişikliklerin '
                       'yansıtılma zamanı mağaza ve ağ erişimine bağlı olabilir.'},
 'de': {'overview': 'Sie können ohne Registrierung oder Anmeldung spielen. Android verwendet für '
                    'die unten beschriebenen Kaufschecks eine automatisch erstellte technische '
                    'Benutzer-ID.',
        'purchase': 'Apple und Google verarbeiten Zahlungen; Wir erhalten nicht Ihre vollständigen '
                    'Zahlungskartendaten. Wenn die Android-Kaufüberprüfung aktiviert ist, erstellt '
                    'Firebase Authentication automatisch eine technische Benutzer-ID ohne '
                    'Registrierungsbildschirm. App Check verwendet Play Integrity, um den Dienst '
                    'zu schützen. Prüfungen können beim Start, beim Kauf oder bei der '
                    'Wiederherstellung durchgeführt werden. Google verarbeitet '
                    'Authentifizierungs-IP-Adressen, technische Geräteinformationen und '
                    'Integritätstoken. Die App sendet ihre Benutzer-ID, den Google Play-Kauf-Token '
                    'und Produktdetails über HTTPS an unseren Google '
                    'Cloud/Firebase-Verifizierungsdienst. Unser Kaufprotokoll speichert einen '
                    'Einweg-Hash des Kauf-Tokens anstelle des Roh-Tokens. Es erfasst separat die '
                    'technische Benutzer-ID, das Produkt, die Transaktionsdaten, die Region, den '
                    'Lieferstatus, die erworbenen Rechte und den Rückerstattungsstatus. Diese '
                    'Aufzeichnungen validieren Einkäufe und verhindern Betrug oder doppelte '
                    'Prämien. Externe Websites haben ihre eigenen Datenschutzrichtlinien.',
        'retention': 'Kaufbestätigungsaufzeichnungen werden aufbewahrt, um den gekauften Zugriff '
                     'aufrechtzuerhalten und wiederholte Prämien zu verhindern. Durch die '
                     'Deinstallation werden diese Serverdatensätze nicht gelöscht. Wenden Sie sich '
                     'an die unten stehende Adresse, um Zugriff oder Löschung anzufordern. '
                     'Anfragen werden im Rahmen der geltenden Datenschutzrechte und der '
                     'erforderlichen Datenaufbewahrung beurteilt. Die vom Anbieter gespeicherten '
                     'Daten unterliegen außerdem den entsprechenden Google-, Firebase- und '
                     'Store-Richtlinien.',
        'security': 'Lokale Daten werden durch das Betriebssystem geschützt. Für die '
                    'Kaufbestätigung und Firebase-Anfragen wird HTTPS verwendet. '
                    'Gerätesicherungen, Speicheraufzeichnungen und Dienstanbieterdaten bleiben '
                    'möglicherweise bestehen, nachdem die App deinstalliert wurde.',
        'local': 'Spielfortschritt, Einstellungen, Hinweisguthaben, gekaufter Zugang und '
                 'Liefermarkierungen werden auf Ihrem Gerät gespeichert. Abhängig von Ihrem Gerät '
                 'und den Sicherungseinstellungen kann das Betriebssystem eine Kopie behalten oder '
                 'wiederherstellen. Die App liest keine Kontakte, Fotos oder den genauen Standort. '
                 'Begrenzte Android-Kaufdetails werden durch den unten beschriebenen '
                 'Verifizierungsdienst verarbeitet.',
        'analytics': 'Produktionsversionen verwenden Firebase Analytics und Firebase Crashlytics '
                     'für Funktionsnutzung und Zuverlässigkeit. Sie verarbeiten Installations- '
                     'oder Sitzungskennungen, Spielinteraktionen, Kauf- und Werbeergebnisse, '
                     'technische App-/Gerätedaten und Absturzdiagnosen. Der Zugriff auf '
                     'Analytics-Werbekennungen und die Werbepersonalisierungssignale sind '
                     'deaktiviert. Firebase Remote Config verwendet eine '
                     'Firebase-Installationskennung und technische Informationen, um einen '
                     'optionalen Katalog „Weitere Spiele“ abzurufen. Diese Dienste unterscheiden '
                     'sich von der Android-Kaufauthentifizierung und -Verifizierung.',
        'chess_terms': 'Verfügbare Produkte werden mit dem vom Geschäft angegebenen Preis '
                       'angezeigt. Verbrauchbare Hinweispakete enthalten 10, 50 oder 200 Hinweise. '
                       'Premium entfernt automatische Anzeigen; Optionale Anzeigen mit Prämie '
                       'bleiben weiterhin verfügbar. Der erste berechtigte Kauf beinhaltet '
                       'einmalig 60 Hinweise; Durch die Wiederherstellung von Premium wird der '
                       'Bonus nicht erneut gewährt. Durch die Wiederherstellung werden verbrauchte '
                       'Hinweise nicht wiederhergestellt. Apple und Google kümmern sich um '
                       'Zahlungen und Rückerstattungen. Bei der Android-Kaufbestätigung wird der '
                       'Transaktions- und Rückerstattungsstatus über den in der '
                       'Datenschutzrichtlinie beschriebenen Dienst überprüft. Die Speicher- und '
                       'Netzwerkverfügbarkeit kann sich darauf auswirken, wann Änderungen '
                       'berücksichtigt werden.'},
 'es': {'overview': 'Puedes jugar sin registrarte ni iniciar sesión. Android utiliza una '
                    'identificación de usuario técnica creada automáticamente para las '
                    'comprobaciones de compra que se describen a continuación.',
        'purchase': 'Apple y Google procesan pagos; No recibimos los datos completos de su tarjeta '
                    'de pago. Cuando la verificación de compra de Android está habilitada, '
                    'Firebase Authentication crea una identificación de usuario técnica automática '
                    'sin una pantalla de registro. App Check utiliza Play Integrity para proteger '
                    'el servicio. Las comprobaciones pueden ejecutarse al inicio, la compra o la '
                    'restauración. Google procesa direcciones IP de autenticación, información '
                    'técnica del dispositivo y tokens de integridad. La aplicación envía su ID de '
                    'usuario, token de compra Google Play y detalles del producto a nuestro '
                    'servicio de verificación Google Cloud/Firebase a través de HTTPS. Nuestro '
                    'libro de compras almacena un hash unidireccional del token de compra en lugar '
                    'del token sin formato. Registra por separado la identificación técnica del '
                    'usuario, el producto, las fechas de la transacción, la región, el estado de '
                    'entrega, los derechos adquiridos y el estado del reembolso. Estos registros '
                    'validan las compras y previenen fraudes o recompensas duplicadas. Los sitios '
                    'externos tienen sus propias políticas de privacidad.',
        'retention': 'Los registros de verificación de compras se mantienen para mantener el '
                     'acceso adquirido y evitar recompensas repetidas. La desinstalación no '
                     'elimina estos registros del servidor. Comuníquese con la dirección a '
                     'continuación para solicitar acceso o eliminación; Las solicitudes se evalúan '
                     'según los derechos de privacidad aplicables y la retención de registros '
                     'necesaria. Los datos retenidos por el proveedor también están sujetos a las '
                     'políticas pertinentes de Google, Firebase y la tienda.',
        'security': 'Los datos locales están protegidos por el sistema operativo. Las solicitudes '
                    'de verificación de compra y Firebase utilizan HTTPS. Las copias de seguridad '
                    'del dispositivo, los registros de la tienda y los datos del proveedor de '
                    'servicios pueden permanecer después de desinstalar la aplicación.',
        'local': 'El progreso del juego, la configuración, el saldo de pistas, el acceso comprado '
                 'y los marcadores de entrega se guardan en su dispositivo. Dependiendo de su '
                 'dispositivo y de la configuración de la copia de seguridad, el sistema operativo '
                 'puede retener o restaurar una copia. La aplicación no lee contactos, fotos ni '
                 'ubicación precisa. Los detalles limitados de compra de Android son procesados '
                 'por el servicio de verificación que se describe a continuación.',
        'analytics': 'Las versiones de producción utilizan Firebase Analytics y Firebase '
                     'Crashlytics para el uso de funciones y la confiabilidad. Procesan '
                     'identificadores de instalación o sesión, interacciones de juego, resultados '
                     'de compras y publicidad, datos técnicos de aplicaciones/dispositivos y '
                     'diagnósticos de fallos. El acceso al identificador de publicidad de '
                     'Analytics y las señales de personalización de publicidad están '
                     'deshabilitados. Firebase Remote Config utiliza un identificador de '
                     'instalación de Firebase e información técnica para obtener un catálogo '
                     'opcional de Más juegos. Estos servicios son distintos de la autenticación y '
                     'verificación de compras de Android.',
        'chess_terms': 'Los productos disponibles se muestran con el precio facilitado por la '
                       'tienda. Los paquetes de pistas consumibles contienen 10, 50 o 200 pistas. '
                       'Premium elimina los anuncios automáticos; Los anuncios bonificados '
                       'opcionales siguen estando disponibles. Su primera compra elegible incluye '
                       '60 pistas una vez; restaurar Premium no otorga el bono nuevamente. '
                       'Restaurar no repone las pistas gastadas. Apple y Google manejan pagos y '
                       'reembolsos. La verificación de compras de Android verifica el estado de '
                       'las transacciones y los reembolsos a través del servicio descrito en la '
                       'Política de Privacidad; La disponibilidad de la tienda y la red puede '
                       'afectar el momento en que se reflejan los cambios.'},
 'fr': {'overview': 'Vous pouvez jouer sans vous inscrire ni vous connecter. Les vérifications des '
                    'achats sur Android utilisent un identifiant technique créé automatiquement, '
                    'comme expliqué ci-dessous.',
        'purchase': 'Apple et Google traitent les paiements\xa0; nous ne recevons pas les détails '
                    'complets de votre carte de paiement. Lorsque la vérification des achats '
                    'Android est activée, Firebase Authentication crée un identifiant '
                    "d'utilisateur technique automatique sans écran d'inscription. App Check "
                    'utilise Play Integrity pour protéger le service. Les vérifications peuvent '
                    "être exécutées au démarrage, à l'achat ou à la restauration. Google traite "
                    "les adresses IP d'authentification, les informations techniques sur les "
                    "appareils et les jetons d'intégrité. L'application envoie son identifiant "
                    "utilisateur, son jeton d'achat Google Play et les détails du produit à notre "
                    'service de vérification Google Cloud/Firebase via HTTPS. Notre registre '
                    "d'achat stocke un hachage unidirectionnel du jeton d'achat au lieu du jeton "
                    "brut. Il enregistre séparément l'ID utilisateur technique, le produit, les "
                    "dates de transaction, la région, l'état de livraison, les droits achetés et "
                    "l'état de remboursement. Ces enregistrements valident les achats et évitent "
                    'la fraude ou les récompenses en double. Les sites externes ont leurs propres '
                    'politiques de confidentialité.',
        'retention': 'Les enregistrements de vérification des achats sont conservés pour conserver '
                     "l'accès acheté et éviter les récompenses répétées. La désinstallation ne "
                     "supprime pas ces enregistrements de serveur. Contactez l'adresse ci-dessous "
                     "pour demander l'accès ou la suppression\xa0; les demandes sont évaluées en "
                     'fonction des droits à la vie privée applicables et de la conservation '
                     'nécessaire des dossiers. Les données détenues par le fournisseur sont '
                     'également soumises aux politiques pertinentes de Google, Firebase et du '
                     'magasin.',
        'security': "Les données locales sont protégées par le système d'exploitation. La "
                    'vérification des achats et les demandes Firebase utilisent HTTPS. Les '
                    "sauvegardes de l'appareil, les enregistrements du magasin et les données du "
                    'fournisseur de services peuvent rester après la désinstallation de '
                    "l'application.",
        'local': 'La progression du jeu, les paramètres, le solde des indices, les accès achetés '
                 'et les marqueurs de livraison sont conservés sur votre appareil. En fonction de '
                 "votre appareil et des paramètres de sauvegarde, le système d'exploitation peut "
                 "conserver ou restaurer une copie. L'application ne lit pas les contacts, les "
                 'photos ou la localisation précise. Les détails limités des achats Android sont '
                 'traités par le service de vérification décrit ci-dessous.',
        'analytics': 'Les versions de production utilisent Firebase Analytics et Firebase '
                     "Crashlytics pour l'utilisation des fonctionnalités et la fiabilité. Ils "
                     'traitent les identifiants d’installation ou de session, les interactions de '
                     'jeu, les résultats d’achat et de publicité, les données techniques des '
                     'applications/appareils et les diagnostics de crash. L’accès aux identifiants '
                     'publicitaires Analytics et les signaux de personnalisation publicitaire sont '
                     "désactivés. Firebase Remote Config utilise un identifiant d'installation "
                     'Firebase et des informations techniques pour récupérer un catalogue Plus de '
                     "jeux facultatif. Ces services sont distincts de l'authentification et de la "
                     'vérification des achats Android.',
        'chess_terms': 'Les produits disponibles sont affichés avec le prix fourni par le magasin. '
                       "Les packs d'indices consommables contiennent 10, 50 ou 200 indices. "
                       'Premium supprime les publicités automatiques\xa0; Les annonces avec '
                       'récompense facultatives restent disponibles. Son premier achat éligible '
                       "comprend 60 indices une fois\xa0; la restauration de Premium n'accorde "
                       'plus le bonus. La restauration ne reconstitue pas les indices dépensés. '
                       'Apple et Google gèrent les paiements et les remboursements. La '
                       'vérification des achats Android vérifie le statut de la transaction et du '
                       'remboursement via le service décrit dans la politique de '
                       'confidentialité\xa0; la disponibilité du magasin et du réseau peut '
                       'affecter le moment où les changements sont reflétés.'},
 'it': {'overview': "Puoi giocare senza registrarti o effettuare l'accesso. Android utilizza un ID "
                    'utente tecnico creato automaticamente per i controlli di acquisto descritti '
                    'di seguito.',
        'purchase': 'Apple e Google elaborano i pagamenti; non riceviamo i dettagli completi della '
                    "tua carta di pagamento. Quando la verifica dell'acquisto su Android è "
                    'abilitata, Firebase Authentication crea un ID utente tecnico automatico senza '
                    'schermata di registrazione. App Check utilizza Play Integrity per proteggere '
                    "il servizio. I controlli possono essere eseguiti all'avvio, all'acquisto o al "
                    'ripristino. Google elabora indirizzi IP di autenticazione, informazioni '
                    "tecniche sul dispositivo e token di integrità. L'app invia il proprio ID "
                    'utente, il token di acquisto Google Play e i dettagli del prodotto al nostro '
                    'servizio di verifica Google Cloud/Firebase tramite HTTPS. Il nostro registro '
                    'degli acquisti memorizza un hash unidirezionale del token di acquisto anziché '
                    "il token grezzo. Registra separatamente l'ID utente tecnico, il prodotto, le "
                    'date della transazione, la regione, lo stato di consegna, i diritti '
                    'acquistati e lo stato del rimborso. Questi record convalidano gli acquisti e '
                    'prevengono frodi o premi duplicati. I siti esterni hanno le proprie politiche '
                    'sulla privacy.',
        'retention': 'I record di verifica degli acquisti vengono conservati per mantenere '
                     "l'accesso acquistato ed evitare premi ripetuti. La disinstallazione non "
                     "elimina questi record del server. Contattare l'indirizzo sottostante per "
                     "richiedere l'accesso o la cancellazione; le richieste vengono valutate in "
                     'base ai diritti sulla privacy applicabili e alla necessaria conservazione '
                     'dei registri. I dati detenuti dal fornitore sono inoltre soggetti alle norme '
                     'pertinenti di Google, Firebase e del negozio.',
        'security': "I dati locali sono protetti dal sistema operativo. La verifica dell'acquisto "
                    'e le richieste Firebase utilizzano HTTPS. I backup del dispositivo, i record '
                    "dell'archivio e i dati del fornitore di servizi potrebbero rimanere dopo la "
                    "disinstallazione dell'app.",
        'local': 'I progressi di gioco, le impostazioni, il saldo dei suggerimenti, gli accessi '
                 'acquistati e gli indicatori di consegna vengono conservati sul tuo dispositivo. '
                 'A seconda del dispositivo e delle impostazioni di backup, il sistema operativo '
                 "potrebbe conservare o ripristinare una copia. L'app non legge contatti, foto o "
                 'posizione precisa. I dettagli relativi agli acquisti Android limitati vengono '
                 'elaborati dal servizio di verifica descritto di seguito.',
        'analytics': 'Le versioni di produzione utilizzano Firebase Analytics e Firebase '
                     "Crashlytics per l'utilizzo delle funzionalità e l'affidabilità. Elaborano "
                     'identificatori di installazione o sessione, interazioni di gioco, risultati '
                     'di acquisto e pubblicità, dati tecnici di app/dispositivo e diagnostica '
                     "degli arresti anomali. L'accesso agli identificatori pubblicitari di "
                     'Analytics e gli indicatori di personalizzazione della pubblicità sono '
                     'disabilitati. Firebase Remote Config utilizza un identificatore di '
                     'installazione Firebase e informazioni tecniche per recuperare un catalogo '
                     "Altri giochi opzionale. Questi servizi sono distinti dall'autenticazione e "
                     'dalla verifica degli acquisti Android.',
        'chess_terms': 'I prodotti disponibili sono mostrati con il prezzo fornito dal negozio. I '
                       'pacchetti di suggerimenti consumabili contengono 10, 50 o 200 '
                       'suggerimenti. Premium rimuove gli annunci automatici; gli annunci con '
                       'premio opzionali rimangono disponibili. Il suo primo acquisto idoneo '
                       'include 60 suggerimenti una volta; il ripristino di Premium non garantisce '
                       'nuovamente il bonus. Il ripristino non ripristina i suggerimenti spesi. '
                       "Apple e Google gestiscono pagamenti e rimborsi. La verifica dell'acquisto "
                       'Android controlla lo stato delle transazioni e dei rimborsi attraverso il '
                       'servizio descritto nella Privacy Policy; la disponibilità del negozio e '
                       'della rete può influire sul momento in cui le modifiche vengono '
                       'applicate.'},
 'pt': {'overview': 'Você pode jogar sem se registrar ou fazer login. O Android usa um ID de '
                    'usuário técnico criado automaticamente para os cheques de compra descritos '
                    'abaixo.',
        'purchase': 'Apple e Google processam pagamentos; não recebemos os detalhes completos do '
                    'seu cartão de pagamento. Quando a verificação de compra do Android está '
                    'habilitada, Firebase Authentication cria um ID de usuário técnico automático '
                    'sem tela de registro. App Check usa Play Integrity para proteger o serviço. '
                    'As verificações podem ser executadas na inicialização, compra ou restauração. '
                    'O Google processa endereços IP de autenticação, informações técnicas de '
                    'dispositivos e tokens de integridade. O aplicativo envia seu ID de usuário, '
                    'token de compra Google Play e detalhes do produto para nosso serviço de '
                    'verificação Google Cloud/Firebase por meio de HTTPS. Nosso livro de compras '
                    'armazena um hash unilateral do token de compra em vez do token bruto. Ele '
                    'registra separadamente o ID técnico do usuário, produto, datas de transação, '
                    'região, status de entrega, direitos adquiridos e status de reembolso. Esses '
                    'registros validam as compras e evitam fraudes ou recompensas duplicadas. '
                    'Sites externos possuem suas próprias políticas de privacidade.',
        'retention': 'Os registros de verificação de compra são mantidos para manter o acesso '
                     'adquirido e evitar recompensas repetidas. A desinstalação não exclui esses '
                     'registros do servidor. Entre em contato com o endereço abaixo para solicitar '
                     'acesso ou exclusão; as solicitações são avaliadas de acordo com os direitos '
                     'de privacidade aplicáveis e a retenção de registros necessária. Os dados '
                     'mantidos pelo provedor também estão sujeitos às políticas relevantes do '
                     'Google, Firebase e da loja.',
        'security': 'Os dados locais são protegidos pelo sistema operacional. A verificação de '
                    'compra e as solicitações do Firebase usam HTTPS. Backups de dispositivos, '
                    'registros de armazenamento e dados do provedor de serviços podem permanecer '
                    'após a desinstalação do aplicativo.',
        'local': 'O progresso do jogo, as configurações, o saldo das dicas, o acesso adquirido e '
                 'os marcadores de entrega são mantidos no seu dispositivo. Dependendo do seu '
                 'dispositivo e das configurações de backup, o sistema operacional pode reter ou '
                 'restaurar uma cópia. O aplicativo não lê contatos, fotos ou localização precisa. '
                 'Os detalhes limitados da compra do Android são processados pelo serviço de '
                 'verificação descrito abaixo.',
        'analytics': 'As versões de produção usam Firebase Analytics e Firebase Crashlytics para '
                     'uso de recursos e confiabilidade. Eles processam identificadores de '
                     'instalação ou sessão, interações de jogo, resultados de compras e '
                     'publicidade, dados técnicos de aplicativos/dispositivos e diagnósticos de '
                     'falhas. O acesso ao identificador de publicidade do Analytics e os sinais de '
                     'personalização de publicidade estão desativados. Firebase Remote Config usa '
                     'um identificador de instalação do Firebase e informações técnicas para '
                     'buscar um catálogo opcional de Mais Jogos. Esses serviços são distintos da '
                     'autenticação e verificação de compras do Android.',
        'chess_terms': 'Os produtos disponíveis são apresentados com o preço fornecido pela loja. '
                       'Os pacotes de dicas consumíveis contêm 10, 50 ou 200 dicas. Premium remove '
                       'anúncios automáticos; anúncios premiados opcionais permanecem disponíveis. '
                       'Sua primeira compra elegível inclui 60 dicas uma vez; restaurar o Premium '
                       'não concede o bônus novamente. A restauração não repõe dicas gastas. A '
                       'Apple e o Google cuidam dos pagamentos e reembolsos. A verificação de '
                       'compra do Android verifica o status da transação e do reembolso por meio '
                       'do serviço descrito na Política de Privacidade; a disponibilidade da loja '
                       'e da rede pode afetar o momento em que as alterações são refletidas.'},
 'ru': {'overview': 'Вы можете играть без регистрации и входа в систему. Android использует '
                    'автоматически создаваемый технический идентификатор пользователя для проверок '
                    'покупок, описанных ниже.',
        'purchase': 'Apple и Google обрабатывают платежи; мы не получаем полные данные вашей '
                    'платежной карты. Когда проверка покупки Android включена, Firebase '
                    'Authentication автоматически создает технический идентификатор пользователя '
                    'без экрана регистрации. App Check использует Play Integrity для защиты '
                    'службы. Проверки могут выполняться при запуске, покупке или восстановлении. '
                    'Google обрабатывает IP-адреса аутентификации, информацию о технических '
                    'устройствах и токены целостности. Приложение отправляет свой идентификатор '
                    'пользователя, токен покупки Google Play и сведения о продукте в нашу службу '
                    'проверки Google Cloud/Firebase через HTTPS. В нашей книге покупок хранится '
                    'односторонний хеш токена покупки вместо необработанного токена. Он отдельно '
                    'записывает идентификатор технического пользователя, продукт, даты транзакций, '
                    'регион, статус доставки, приобретенные права и статус возврата. Эти записи '
                    'подтверждают покупки и предотвращают мошенничество или дублирование '
                    'вознаграждений. Внешние сайты имеют собственную политику конфиденциальности.',
        'retention': 'Записи о проверке покупок сохраняются для сохранения приобретенного доступа '
                     'и предотвращения повторных вознаграждений. Удаление не удаляет эти записи '
                     'сервера. Свяжитесь с указанным ниже адресом, чтобы запросить доступ или '
                     'удаление; запросы оцениваются в соответствии с применимыми правами на '
                     'конфиденциальность и необходимым сохранением записей. Данные, хранящиеся у '
                     'поставщика, также регулируются соответствующими политиками Google, Firebase '
                     'и магазина.',
        'security': 'Локальные данные защищены операционной системой. Для проверки покупок и '
                    'запросов Firebase используется HTTPS. Резервные копии устройства, записи '
                    'магазина и данные поставщика услуг могут остаться после удаления приложения.',
        'local': 'Ход игры, настройки, баланс подсказок, маркеры купленного доступа и доставки '
                 'сохраняются на вашем устройстве. В зависимости от вашего устройства и настроек '
                 'резервного копирования операционная система может сохранить или восстановить '
                 'копию. Приложение не считывает контакты, фотографии и точное местоположение. '
                 'Детали ограниченной покупки Android обрабатываются службой проверки, описанной '
                 'ниже.',
        'analytics': 'В производственных версиях используются Firebase Analytics и Firebase '
                     'Crashlytics для обеспечения использования функций и надежности. Они '
                     'обрабатывают идентификаторы установки или сеанса, игровые взаимодействия, '
                     'результаты покупок и рекламы, технические данные приложения/устройства и '
                     'диагностику сбоев. Доступ к рекламным идентификаторам Analytics и сигналы '
                     'персонализации рекламы отключены. Firebase Remote Config использует '
                     'идентификатор установки Firebase и техническую информацию для получения '
                     'дополнительного каталога дополнительных игр. Эти услуги отличаются от '
                     'аутентификации и проверки покупок Android.',
        'chess_terms': 'Доступные товары указаны по цене, указанной в магазине. Расходуемые пакеты '
                       'подсказок содержат 10, 50 или 200 подсказок. Премиум удаляет '
                       'автоматическую рекламу; дополнительные объявления с вознаграждением '
                       'остаются доступными. Первая соответствующая покупка включает в себя 60 '
                       'подсказок один раз; восстановление Премиума не дает бонус снова. '
                       'Восстановление не восполняет потраченные подсказки. Apple и Google '
                       'обрабатывают платежи и возвраты средств. Проверка покупки Android '
                       'проверяет статус транзакции и возврата средств с помощью службы, описанной '
                       'в Политике конфиденциальности; Доступность магазина и сети может повлиять '
                       'на отражение изменений.'},
 'id': {'overview': 'Anda dapat bermain tanpa mendaftar atau masuk. Android menggunakan ID '
                    'pengguna teknis yang dibuat secara otomatis untuk cek pembelian yang '
                    'dijelaskan di bawah.',
        'purchase': 'Apple dan Google memproses pembayaran; kami tidak menerima rincian lengkap '
                    'kartu pembayaran Anda. Saat verifikasi pembelian Android diaktifkan, Firebase '
                    'Authentication membuat ID pengguna teknis otomatis tanpa layar registrasi. '
                    'App Check menggunakan Play Integrity untuk melindungi layanan. Pemeriksaan '
                    'dapat dijalankan saat permulaan, pembelian, atau pemulihan. Google memproses '
                    'alamat IP autentikasi, informasi perangkat teknis, dan token integritas. '
                    'Aplikasi mengirimkan ID penggunanya, token pembelian Google Play, dan detail '
                    'produk ke layanan verifikasi Google Cloud/Firebase kami melalui HTTPS. Buku '
                    'besar pembelian kami menyimpan hash satu arah dari token pembelian, bukan '
                    'token mentah. Ini secara terpisah mencatat ID pengguna teknis, produk, '
                    'tanggal transaksi, wilayah, status pengiriman, hak pembelian, dan status '
                    'pengembalian dana. Catatan ini memvalidasi pembelian dan mencegah penipuan '
                    'atau duplikat hadiah. Situs eksternal memiliki kebijakan privasinya sendiri.',
        'retention': 'Catatan verifikasi pembelian disimpan untuk mempertahankan akses pembelian '
                     'dan mencegah hadiah berulang. Menghapus instalasi tidak menghapus catatan '
                     'server ini. Hubungi alamat di bawah ini untuk meminta akses atau '
                     'penghapusan; permintaan dinilai berdasarkan hak privasi yang berlaku dan '
                     'penyimpanan catatan yang diperlukan. Data yang disimpan penyedia juga tunduk '
                     'pada kebijakan Google, Firebase, dan toko yang relevan.',
        'security': 'Data lokal dilindungi oleh sistem operasi. Verifikasi pembelian dan '
                    'permintaan Firebase menggunakan HTTPS. Cadangan perangkat, catatan '
                    'penyimpanan, dan data penyedia layanan mungkin tetap ada setelah aplikasi '
                    'dicopot pemasangannya.',
        'local': 'Kemajuan game, pengaturan, saldo petunjuk, akses yang dibeli, dan penanda '
                 'pengiriman disimpan di perangkat Anda. Tergantung pada perangkat dan pengaturan '
                 'cadangan Anda, sistem operasi mungkin menyimpan atau memulihkan salinan. '
                 'Aplikasi ini tidak membaca kontak, foto, atau lokasi persisnya. Detail pembelian '
                 'Android terbatas diproses oleh layanan verifikasi yang dijelaskan di bawah.',
        'analytics': 'Rilis produksi menggunakan Firebase Analytics dan Firebase Crashlytics untuk '
                     'penggunaan fitur dan keandalan. Mereka memproses pengidentifikasi instalasi '
                     'atau sesi, interaksi gameplay, hasil pembelian dan periklanan, data teknis '
                     'aplikasi/perangkat, dan diagnostik kerusakan. Akses pengidentifikasi iklan '
                     'Analytics dan sinyal personalisasi iklan dinonaktifkan. Firebase Remote '
                     'Config menggunakan ID instalasi Firebase dan informasi teknis untuk '
                     'mengambil katalog Game Lainnya opsional. Layanan ini berbeda dari '
                     'autentikasi dan verifikasi pembelian Android.',
        'chess_terms': 'Produk yang tersedia ditampilkan dengan harga yang disediakan oleh toko. '
                       'Paket petunjuk yang dapat dikonsumsi berisi 10, 50, atau 200 petunjuk. '
                       'Premium menghapus iklan otomatis; iklan reward opsional tetap tersedia. '
                       'Pembelian pertama yang memenuhi syarat mencakup 60 petunjuk satu kali; '
                       'memulihkan Premium tidak memberikan bonus lagi. Pemulihan tidak mengisi '
                       'kembali petunjuk yang dihabiskan. Apple dan Google menangani pembayaran '
                       'dan pengembalian dana. Verifikasi pembelian Android memeriksa status '
                       'transaksi dan pengembalian dana melalui layanan yang dijelaskan dalam '
                       'Kebijakan Privasi; ketersediaan toko dan jaringan dapat mempengaruhi '
                       'ketika perubahan diterapkan.'},
 'ja': {'overview': '登録やログインをせずにプレイできます。Android の購入確認では、以下に説明する自動生成の技術用ユーザー ID を使用します。',
        'purchase': 'Apple と Google が支払いを処理します。私たちはあなたの支払いカードの詳細を完全には受け取っていません。 Android '
                    '購入検証が有効になっている場合、Firebase Authentication は登録画面なしで技術用のユーザー ID を自動的に作成します。 App '
                    'Check は、Play Integrity を使用してサービスを保護します。チェックは起動時、購入時、または復元時に実行される場合があります。 '
                    'Google は認証 IP アドレス、技術的なデバイス情報、整合性トークンを処理します。アプリは、ユーザー ID、Google Play '
                    '購入トークン、製品の詳細を HTTPS 経由で Google Cloud/Firebase '
                    '検証サービスに送信します。私たちの購入台帳には、生のトークンではなく、購入トークンの一方向ハッシュが保存されます。技術ユーザー '
                    'ID、製品、取引日、地域、付与状況、購入した権利、返金状況が個別に記録されます。これらの記録は購入を検証し、詐欺や特典の重複を防ぎます。外部サイトには独自のプライバシー '
                    'ポリシーがあります。',
        'retention': '購入確認記録は、購入したアクセスを維持し、特典の繰り返しを防ぐために保管されます。アンインストールしても、これらのサーバー '
                     'レコードは削除されません。アクセスまたは削除をリクエストするには、以下のアドレスに連絡してください。リクエストは、適用されるプライバシー権と必要な記録保持に基づいて評価されます。プロバイダーが保持するデータには、関連する '
                     'Google、Firebase、ストアのポリシーも適用されます。',
        'security': 'ローカル データはオペレーティング システムによって保護されています。購入確認と Firebase リクエストでは HTTPS '
                    'を使用します。アプリのアンインストール後も、デバイスのバックアップ、ストアの記録、サービスプロバイダーのデータが残る場合があります。',
        'local': 'ゲームの進行状況、設定、ヒント残高、購入したアクセス、配信マーカーはデバイスに保存されます。デバイスとバックアップの設定によっては、オペレーティング '
                 'システムがコピーを保持または復元する場合があります。アプリは連絡先、写真、正確な位置情報を読み取りません。制限付きの Android '
                 '購入詳細は、以下に説明する検証サービスによって処理されます。',
        'analytics': '製品リリースでは、機能の使用法と信頼性を確保するために Firebase Analytics および Firebase Crashlytics '
                     'を使用します。これらは、インストールまたはセッションの識別子、ゲームプレイのインタラクション、購入と広告の結果、技術的なアプリ/デバイスのデータ、およびクラッシュ診断を処理します。分析の広告識別子アクセスと広告パーソナライゼーションシグナルは無効になっています。 '
                     'Firebase Remote Config は、Firebase インストール識別子と技術情報を使用して、オプションのその他のゲーム '
                     'カタログを取得します。これらのサービスは、Android の購入認証および検証とは異なります。',
        'chess_terms': '在庫のある商品はストアが提供する価格で表示されます。消耗品ヒント パックには、10、50、または 200 '
                       '個のヒントが含まれています。プレミアムでは自動広告が削除されます。オプションのリワード広告は引き続きご利用いただけます。対象となる最初の '
                       'Premium 購入時に限り、60 '
                       '個のヒントが一度だけ付与されます。プレミアムを復元してもボーナスは再度付与されません。復元では、使用済みのヒントは補充されません。 Apple と '
                       'Google が支払いと返金を処理します。 Android の購入確認では、プライバシー '
                       'ポリシーに記載されているサービスを通じて取引と返金のステータスを確認します。ストアとネットワークの可用性は、変更がいつ反映されるかに影響を与える可能性があります。'},
 'ko': {'overview': '등록이나 로그인 없이 플레이할 수 있습니다. Android는 아래 설명된 구매 확인을 위해 자동으로 생성된 기술 사용자 ID를 사용합니다.',
        'purchase': 'Apple 및 Google이 결제를 처리합니다. 우리는 귀하의 전체 지불 카드 정보를 받지 못합니다. Android 구매 확인이 활성화되면 '
                    'Firebase Authentication은 등록 화면 없이 자동 기술 사용자 ID를 생성합니다. App Check는 Play '
                    'Integrity를 사용하여 서비스를 보호합니다. 시작, 구매 또는 복원 시 검사가 실행될 수 있습니다. Google은 인증 IP 주소, '
                    '기술 장치 정보 및 무결성 토큰을 처리합니다. 앱은 HTTPS를 통해 사용자 ID, Google Play 구매 토큰 및 제품 세부 정보를 '
                    'Google Cloud/Firebase 확인 서비스로 보냅니다. 구매 원장은 원시 토큰 대신 구매 토큰의 단방향 해시를 저장합니다. 기술적 '
                    '사용자 ID, 제품, 거래일자, 지역, 지급 상태, 구매권한, 환불상태 등을 별도로 기록합니다. 이러한 기록은 구매를 확인하고 사기나 중복 '
                    '보상을 방지합니다. 외부 사이트에는 자체 개인 정보 보호 정책이 있습니다.',
        'retention': '구매한 접속 권한을 유지하고 중복 보상을 방지하기 위해 구매 인증 기록을 보관합니다. 제거해도 이러한 서버 기록은 삭제되지 않습니다. '
                     '접근 또는 삭제를 요청하려면 아래 주소로 연락하세요. 요청은 해당 개인 정보 보호 권리 및 필요한 기록 보존에 따라 평가됩니다. '
                     '제공업체가 보유한 데이터에는 관련 Google, Firebase 및 스토어 정책도 적용됩니다.',
        'security': '로컬 데이터는 운영 체제에 의해 보호됩니다. 구매 확인 및 Firebase 요청은 HTTPS를 사용합니다. 앱을 제거한 후에도 기기 백업, '
                    '매장 기록, 서비스 제공업체 데이터가 남아 있을 수 있습니다.',
        'local': '게임 진행 상황, 설정, 힌트 잔액, 구매한 액세스 및 배달 마커가 장치에 보관됩니다. 장치 및 백업 설정에 따라 운영 체제에서 복사본을 '
                 '유지하거나 복원할 수 있습니다. 앱은 연락처, 사진 또는 정확한 위치를 읽지 않습니다. 제한된 Android 구매 세부정보는 아래 설명된 확인 '
                 '서비스를 통해 처리됩니다.',
        'analytics': '프로덕션 릴리스는 기능 사용 및 안정성을 위해 Firebase Analytics 및 Firebase Crashlytics를 사용합니다. '
                     '설치 또는 세션 식별자, 게임 플레이 상호 작용, 구매 및 광고 결과, 기술 앱/장치 데이터 및 충돌 진단을 처리합니다. 분석 광고 '
                     '식별자 액세스 및 광고 개인화 신호가 비활성화되었습니다. Firebase Remote Config는 Firebase 설치 식별자와 기술 '
                     '정보를 사용하여 선택적인 추가 게임 카탈로그를 가져옵니다. 이러한 서비스는 Android 구매 인증 및 확인과는 다릅니다.',
        'chess_terms': '구매 가능한 제품은 매장에서 제공하는 가격과 함께 표시됩니다. 소모형 힌트 팩에는 10, 50 또는 200개의 힌트가 포함되어 '
                       '있습니다. 프리미엄은 자동 광고를 제거합니다. 선택적 보상형 광고는 계속 사용할 수 있습니다. 첫 번째 적격 구매에는 60개의 힌트가 '
                       '한 번 포함됩니다. 프리미엄을 복원해도 보너스가 다시 부여되지는 않습니다. 복원 시 사용한 힌트가 보충되지 않습니다. Apple과 '
                       'Google은 결제 및 환불을 처리합니다. Android 구매 확인은 개인정보 보호정책에 설명된 서비스를 통해 거래 및 환불 상태를 '
                       '확인합니다. 매장 및 네트워크 가용성은 변경 사항이 반영되는 시점에 영향을 미칠 수 있습니다.'}}
