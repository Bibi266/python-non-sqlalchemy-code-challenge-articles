class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        """Retourne la liste de tous les articles écrits par cet auteur."""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Retourne la liste de tous les magazines dans lesquels l’auteur a publié."""
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        """Crée et retourne un nouvel article lié à l’auteur et au magazine."""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Retourne la liste unique des catégories (topics) des magazines de l’auteur."""
        if len(self.articles()) == 0:
            return None
        return list(set([article.magazine.category for article in self.articles()]))


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        """Retourne la liste des articles publiés dans ce magazine."""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Retourne la liste unique des auteurs qui ont écrit pour ce magazine."""
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        """Retourne la liste des titres d’articles pour ce magazine."""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """Retourne la liste des auteurs ayant écrit plus de 2 articles dans ce magazine."""
        authors = []
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                authors.append(author)
        return authors if authors else None


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title