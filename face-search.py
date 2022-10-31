import cv2


# メイン関数
def Main():
    # 顔検出メイン関数
    FaceSelarchMain()


# 顔検出メイン関数
def FaceSelarchMain():
    # ビデオキャプチャする
    cap = cv2.VideoCapture(0)

    while True:
        # ビデオを画像に変換する
        ret, image = cap.read()

        # 画像描画する
        cv2.imshow("Frame", image)

        # キー入力する
        key = cv2.waitKey(1)

        # spaceキーで終了する
        if key == 32:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    Main()
