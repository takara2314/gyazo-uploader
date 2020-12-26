# https://github.com/takara2314/gyazo-uploader の下にある説明を確認してね☆

from gyazo import Api
import json

# XXXの部分にアクセストークンを入れる
gyazo_client = Api(access_token="XXX")

img_url = ""

# withスコープから外れたら sample.png が閉じられる
with open("sample.png", "rb") as f:
    # sample.png をGyazoにアップロードし、返ってきたものをresponseに格納する
    response = gyazo_client.upload_image(f)
    # responseに格納されたものをJSON文字列に変換し、辞書型に変換する
    json_dict = json.loads(response.to_json())
    # キーurlに画像URLが格納されている
    # (変数img_url にも画像URLを入れておくとわかりやすいかも)
    img_url = json_dict["url"]

print("画像URL:", img_url)