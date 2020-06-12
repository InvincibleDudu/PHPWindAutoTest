import time


def save_log(results):
    path = time.strftime("%Y-%m-%d", time.gmtime()) + ".csv"

    f = open(path, 'w', encoding='utf-8')
    for result in results:
        f.write(result + "\n")
    f.close()


def save_log2(results):
    path = "message_log.csv"
    f = open(path, 'w', encoding='utf-8')
    for result in results:
        f.write(result + "\n")
    f.close()


if __name__ == "__main__":
    datas = ["this if my log1",
             "this is my log2"
             ]
    save_log(datas)
    save_log2(datas)
