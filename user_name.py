class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}はルール違反です")

        self.name = name

    def screen_name(self):
        return self.name.upper()

# UseNameクラスのインスタンス化
tanaka = UserName(name="tanaka")
# 出力
print(tanaka.screen_name())
