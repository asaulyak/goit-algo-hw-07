class Comment:
    def __init__(self, comment:str, author:str):
        self.comment = comment
        self.author = author
        self.is_deleted = False
        self.replies = []


    def display(self, indent: int = 0):
        author = f'{self.author}: ' if not self.is_deleted else ''
        print('  ' * indent, f'{author}{self.comment}')

        for reply in self.replies:
            reply.display(indent + 2)


    def add_reply(self, comment):
        self.replies.append(comment)


    def remove_reply(self):
        self.is_deleted = True
        self.comment = 'Цей коментар було видалено.'



root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні на що...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()