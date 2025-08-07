class Book:
    all = []

    def __init__(self, title):
        self.title = title

    def contracts(self):
        return list(self._contracts)
    
    def authors(self):
        return [contract.author for contract in self._contracts]


class Author:
    all = [] 

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all.append(self)
    
    def books(self):
        return [contract.book for contract in self._contracts]   
    
    def contracts(self):
        return list(self._contracts)
    
    def sign_contracts(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all =[]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        # self._author._contracts.append(self)
        # self._book._contracts.append(self)
        Contract.all.append(self)
        
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @classmethod
    def contracts_by_date(self, date):
        return [contracts for contracts in Contract.all if contracts.date == date]