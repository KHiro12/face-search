import cv2


# メイン関数
def Main():
    # 顔検出メイン関数
    FaceSearchMain()


# 顔検出メイン関数
def FaceSearchMain():
    # ビデオキャプチャする
    cap = cv2.VideoCapture(0)

    while True:
        # ビデオを画像に変換する
        ret, image = cap.read()

        # 顔検出
        FaceSearch(image)

        # 画像描画する
        cv2.imshow("Frame", image)

        # キー入力する
        key = cv2.waitKey(1)

        # spaceキーで終了する
        if key == 32:
            break

    cap.release()
    cv2.destroyAllWindows()


# 顔検出
def FaceSearch(img):
    # 顔をHaar like特徴で探索する
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔を検知
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        # 検知した顔を矩形で囲む
        cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,0), 2)



if __name__ == '__main__':
    Main()
