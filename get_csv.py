def get_csv(path):
    posts = []
    f = open(path, 'r', encoding='utf-8')
    for line in f:
        user = {}
        result = [ele.strip() for ele in line.split(",")]
        user["title"] = result[0]
        user["body"] = result[1]
        posts.append(user)
    return posts


if __name__ == "__main__":
    path = "posts.csv"
    print(get_csv(path))
