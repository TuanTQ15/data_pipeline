class Config:

    PROXY_WEBPAGE = "https://free-proxy-list.net/"

    TESTING_URL = "https://google.com"

    REDIS_CONFIG = {
        "host": "redis",
        "port": "6379",
        "db": 0
    }

    REDIS_KEY = "proxies"

    MAX_WORKERS = 50

    NUMBER_OF_PROXIES = 50

    RSS_FEEDS = {
        "vnexpress": [
            "https://vnexpress.net/rss/thoi-su.rss",
            "https://vnexpress.net/rss/kinh-doanh.rss",
            "https://vnexpress.net/rss/giai-tri.rss",
            "https://vnexpress.net/rss/the-thao.rss",
            "https://vnexpress.net/rss/phap-luat.rss",
            "https://vnexpress.net/rss/giao-duc.rss",
            "https://vnexpress.net/rss/suc-khoe.rss",
            "https://vnexpress.net/rss/gia-dinh.rss",
            "https://vnexpress.net/rss/du-lich.rss",
            "https://vnexpress.net/rss/oto-xe-may.rss",
            "https://vnexpress.net/rss/khoa-hoc.rss"
        ],
        "tuoitre": [
            "https://tuoitre.vn/rss/thoi-su.rss",
            "https://tuoitre.vn/rss/kinh-doanh.rss",
            "https://tuoitre.vn/rss/giai-tri.rss",
            "https://tuoitre.vn/rss/the-thao.rss",
            "https://tuoitre.vn/rss/phap-luat.rss",
            "https://tuoitre.vn/rss/giao-duc.rss",
            "https://tuoitre.vn/rss/suc-khoe.rss",
            "https://tuoitre.vn/rss/nhip-song-tre.rss",
            "https://tuoitre.vn/rss/du-lich.rss",
            "https://tuoitre.vn/rss/xe.rss",
            "https://tuoitre.vn/rss/nhip-song-so.rss"
        ],
        "thanhnien": [
            "https://thanhnien.vn/rss/thoi-su-4.rss",
            "https://thanhnien.vn/rss/tai-chinh-kinh-doanh-49.rss",
            "https://thanhnien.vn/rss/giai-tri-285.rss",
            "https://thanhnien.vn/rss/the-thao/bong-da-viet-nam-375.rss",
            "https://thanhnien.vn/rss/thoi-su/phap-luat-5.rss",
            "https://thanhnien.vn/rss/giao-duc-26.rss",
            "https://thanhnien.vn/rss/suc-khoe-65.rss",
            "https://thanhnien.vn/rss/doi-song-17.rss",
            "https://thanhnien.vn/rss/du-lich-234.rss",
            "https://thanhnien.vn/rss/xe-317.rss",
            "https://thanhnien.vn/rss/cong-nghe-12.rss"
        ],     
    
    }

    
    BOOTSTRAP_SERVERS = ["kafka:9092"]

    TOPIC = "rss_news"

    VALIDATOR_CONFIG = {
        "description_length": 10,
        "languages": [
            "en", "pl", "es", "de"
        ]
    }
