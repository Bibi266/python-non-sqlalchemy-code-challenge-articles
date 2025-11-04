from classes.many_to_many import Author, Magazine, Article

author = Author("Carry Bradshaw")
magazine = Magazine("Vogue", "Fashion")
article = Article(author, magazine, "How to wear a tutu with style")

print(f"Auteur : {author.name}")
print(f"Magazine : {magazine.name}")
print(f"Titre : {article.title}")
print(f"Magazines de l'auteur : {[m.name for m in author.magazines()]}")
