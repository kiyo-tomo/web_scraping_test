#日経平均平均株価
nikkei_heikin = ""

#①インポートします。
import requests
from bs4 import BeautifulSoup


def get_nikkei225_now():
    #②HTMLを取得します。
    url = 'https://www.nikkei.com/'
    html = requests.get(url)

    #③HTMLパース用のオブジェクトを作成します。
    soup = BeautifulSoup(html.text, "html.parser")

    #④「span」要素全て抽出します。
    span = soup.find_all("span")

    #⑤「span」要素をループします。
    for tag in span:
        try:
            #⑥「span」要素から「class」をpopしていきます。
            string_ = tag.get("class").pop(0)
            #⑦摘出したclassの文字列にm-miH01C_rateが設定されているかチェックします。
            if string_ in "m-miH01C_rate":
                #⑧tagの文字列(日経平均株価)を取得します。
                nikkei_heikin = tag.string
                #⑨ループ処理を中断します。
                break
        except:
            #⑥'「span」要素から「class」をpopできなかった場合何もしません。
            pass

    return nikkei_heikin


print(get_nikkei225_now())
