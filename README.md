# Odakyu
小田急線の駅の分析

## 詳細
電車で本を読むことを目的としたとき、最も効率良く移動できる駅はどこか を探索する

## 条件
- 全て各駅
- 安くて乗車時間が長い
- 乗車時間は平日と土日の9:00, 11:00, 13:90, 15:00, 17:00, 19:00 乗車で検索したときの乗車時間を考慮に入れる

## 進捗
1. 小田急線の乗り換え案内ページ(https://www.odakyu.jp/change/transfer_result/?targetstart=&roughEstimate=co2&startName=%E7%94%9F%E7%94%B0%28%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C%29&start=&start=&orvCode=0.0.00004682.%E7%94%9F%E7%94%B0%28%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C%29&orvAdd=&startPosType=&orvPosType=1&goalName=%E6%96%B0%E5%AE%BF&goal=&goal=&dnvCode=0.0.00004254.%E6%96%B0%E5%AE%BF&dnvAdd=&goalPosType=&dnvPosType=1&day=20220324&hour=09&minute=00&year=&month=&basis=1&useRomancecar=false&sort=0&wspeed=standard&meth) からスクレイピングすることを試みる
2. ナビタイムがiframeで埋め込まれていて時間や経路はこのページからでは入手できなかった
3. ナビタイム(https://www.navitime.co.jp/transfer/searchlist?orvStationName=%E7%94%9F%E7%94%B0%EF%BC%88%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C%EF%BC%89&orvStationCode=00004682&dnvStationName=%E6%96%B0%E5%AE%BF&dnvStationCode=00004254&month=2022/03&day=24&hour=09&minute=00&basis=1&airplane=1&sprexprs=1&utrexprs=1&othexprs=1&mtrplbus=1&intercitybus=1&ferry=1&sort=4&isrec=1&from=view.transfer.searchlist.tab.recommend) からスクレイピングすることを試みる
4. 出発駅や到着駅を変えるためには、URL内のorvStationName, dnvStationNameを変えても意味がなく、orvStationCode, dnvStationCode を変更する必要があるよう
5. Code一覧が掲載されているページにアクセスできず(NavitimeのAPIを使用するか、小田急線のナビタイム駅コードを手作業で調べるか、ナビタイムの検索ページをSeleniumで操作して駅名だけでページにアクセスする必要がある)
6. Selenium が一番早い気はする。作業は保留