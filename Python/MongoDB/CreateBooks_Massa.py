# MongoDB Non-Fiction
from pymongo import MongoClient

def create_books(title, author, year, pages, language, rating):
    MONGO_URI = "mongodb://localhost:27017/"
    DB_NAME = "Books"
    COLLECTION_NAME = "Non-Fiction"

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    
    new_document = {
    "title": title,
    "author": author,
    "year": year,
    "pages": pages,
    "language": language,
    "rating": rating
}
    insert_result = collection.insert_one(new_document)
    print("Inserted document ID:", insert_result.inserted_id)
    
def add_books_to_database(books_data):
    for book in books_data:
        create_books(
            title=book['title'],
            author=book['author'],
            year=book['year'],
            pages=book['pages'],
            language=book['language'],
            rating=book['rating']
        )
              
books_data = [
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "year": 2011,
        "pages": 443,
        "language": "English",
        "rating": 4.4
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "year": 2018,
        "pages": 352,
        "language": "English",
        "rating": 4.5
    },
    {
        "title": "Becoming",
        "author": "Michelle Obama",
        "year": 2018,
        "pages": 426,
        "language": "English",
        "rating": 4.8
    },
    {
        "title": "Homo Deus: A Brief History of Tomorrow",
        "author": "Yuval Noah Harari",
        "year": 2015,
        "pages": 448,
        "language": "English",
        "rating": 4.5
    },
    {
        "title": "The Body Keeps the Score: Brain, Mind, and Body in the Healing of Trauma",
        "author": "Bessel van der Kolk",
        "year": 2014,
        "pages": 443,
        "language": "English",
        "rating": 4.6
    },
    {
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "year": 2011,
        "pages": 499,
        "language": "English",
        "rating": 4.3
    },
    {
        "title": "12 Rules for Life: An Antidote to Chaos",
        "author": "Jordan B. Peterson",
        "year": 2018,
        "pages": 409,
        "language": "English",
        "rating": 4.7
    },
    {
        "title": "The Subtle Art of Not Giving a F*ck: A Counterintuitive Approach to Living a Good Life",
        "author": "Mark Manson",
        "year": 2016,
        "pages": 224,
        "language": "English",
        "rating": 4.0
    },
    {
        "title": "Bad Blood: Secrets and Lies in a Silicon Valley Startup",
        "author": "John Carreyrou",
        "year": 2018,
        "pages": 339,
        "language": "English",
        "rating": 4.5
    },
    {
        "title": "The Power of Habit: Why We Do What We Do in Life and Business",
        "author": "Charles Duhigg",
        "year": 2012,
        "pages": 371,
        "language": "English",
        "rating": 4.6
    },
    {
        "title": "The Immortal Life of Henrietta Lacks",
        "author": "Rebecca Skloot",
        "year": 2010,
        "pages": 370,
        "language": "English",
        "rating": 4.1
    },
    {
        "title": "Quiet: The Power of Introverts in a World That Can't Stop Talking",
        "author": "Susan Cain",
        "year": 2012,
        "pages": 333,
        "language": "English",
        "rating": 4.0
    },
    {
        "title": "Guns, Germs, and Steel: The Fates of Human Societies",
        "author": "Jared Diamond",
        "year": 1997,
        "pages": 480,
        "language": "English",
        "rating": 4.3
    },
    {
        "title": "Born a Crime: Stories from a South African Childhood",
        "author": "Trevor Noah",
        "year": 2016,
        "pages": 304,
        "language": "English",
        "rating": 4.8
    },
    {
        "title": "The Sixth Extinction: An Unnatural History",
        "author": "Elizabeth Kolbert",
        "year": 2014,
        "pages": 319,
        "language": "English",
        "rating": 4.3
    },
    {
        "title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "year": 1936,
        "pages": 288,
        "language": "English",
        "rating": 4.2
    },
    {
        "title": "The Emperor of All Maladies: A Biography of Cancer",
        "author": "Siddhartha Mukherjee",
        "year": 2010,
        "pages": 571,
        "language": "English",
        "rating": 4.5
    },
    {
        "title": "Man's Search for Meaning",
        "author": "Viktor E. Frankl",
        "year": 1946,
        "pages": 165,
        "language": "English",
        "rating": 4.4
    },
    {
        "title": "Outliers: The Story of Success",
        "author": "Malcolm Gladwell",
        "year": 2008,
        "pages": 309,
        "language": "English",
        "rating": 4.2
    },
    {
        "title": "The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography",
        "author": "Simon Singh",
        "year": 1999,
        "pages": 402,
        "language": "English",
        "rating": 4.2
    },
    {
        "title": "The Warmth of Other Suns: The Epic Story of America's Great Migration",
        "author": "Isabel Wilkerson",
        "year": 2010,
        "pages": 622,
        "language": "English",
        "rating": 4.7
    },
    {
        "title": "The Wright Brothers",
        "author": "David McCullough",
        "year": 2015,
        "pages": 336,
        "language": "English",
        "rating": 4.5
    },
    {
        "title": "The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America",
        "author": "Erik Larson",
        "year": 2003,
        "pages": 447,
        "language": "English",
        "rating": 4.2
    },
    {
        "title": "The Silk Roads: A New History of the World",
        "author": "Peter Frankopan",
        "year": 2015,
        "pages": 672,
        "language": "English",
        "rating": 4.1
    },
    {
        "title": "The Gene: An Intimate History",
        "author": "Siddhartha Mukherjee",
        "year": 2016,
        "pages": 592,
        "language": "English",
        "rating": 4.5
    },
    {
        "title": "The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses",
        "author": "Eric Ries",
        "year": 2011,
        "pages": 336,
        "language": "English",
        "rating": 4.6
    },
    {
        "title": "The Four Agreements: A Practical Guide to Personal Freedom",
        "author": "Don Miguel Ruiz",
        "year": 1997,
        "pages": 160,
        "language": "English",
        "rating": 4.6
    },
    {
        "title": "The Art of War",
        "author": "Sun Tzu",
        "year": "5th century BC",
        "pages": 61,
        "language": "English",
        "rating": 4.1
    },
    {
        "title": "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones",
        "author": "James Clear",
        "year": 2018,
        "pages": 319,
        "language": "English",
        "rating": 4.6
    },
    {
        "title": "The 7 Habits of Highly Effective People: Powerful Lessons in Personal Change",
        "author": "Stephen R. Covey",
        "year": 1989,
        "pages": 381,
        "language": "English",
        "rating": 4.1
    },
    {
        "title": "The Tipping Point: How Little Things Can Make a Big Difference",
        "author": "Malcolm Gladwell",
        "year": 2000,
        "pages": 301,
        "language": "English",
        "rating": 4.1
    },
    {
        "title": "Freakonomics: A Rogue Economist Explores the Hidden Side of Everything",
        "author": "Steven D. Levitt, Stephen J. Dubner",
        "year": 2005,
        "pages": 315,
        "language": "English",
        "rating": 4.1
    },
    {
        "title": "The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail",
        "author": "Clayton M. Christensen",
        "year": 1997,
        "pages": 286,
        "language": "English",
        "rating": 4.0
    },
    {
        "title": "Why We Sleep: Unlocking the Power of Sleep and Dreams",
        "author": "Matthew Walker",
        "year": 2017,
        "pages": 343,
        "language": "English",
        "rating": 4.4
    },
    {
        "title": "Influence: The Psychology of Persuasion",
        "author": "Robert B. Cialdini",
        "year": 1984,
        "pages": 320,
        "language": "English",
        "rating": 4.2
    },
    {
        "title": "The Black Swan: The Impact of the Highly Improbable",
        "author": "Nassim Nicholas Taleb",
        "year": 2007,
        "pages": 444,
        "language": "English",
        "rating": 4.0
    },
    {
        "title": "The Power of Now: A Guide to Spiritual Enlightenment",
        "author": "Eckhart Tolle",
        "year": 1997,
        "pages": 236,
        "language": "English",
        "rating": 4.2
    },
    {
        "title": "Grit: The Power of Passion and Perseverance",
        "author": "Angela Duckworth",
        "year": 2016,
        "pages": 333,
        "language": "English",
        "rating": 4.3
    },
    {
        "title": "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts",
        "author": "Annie Duke",
        "year": 2018,
        "pages": 288,
        "language": "English",
        "rating": 4.3
    },
    {
        "title": "The Selfish Gene",
        "author": "Richard Dawkins",
        "year": 1976,
        "pages": 360,
        "language": "English",
        "rating": 4.1
    },
    {
        "title": "The Power of Vulnerability: Teachings on Authenticity, Connection, and Courage",
        "author": "Brené Brown",
        "year": 2012,
        "pages": 190,
        "language": "English",
        "rating": 4.4
    },
    {
        "title": "How to Change Your Mind: What the New Science of Psychedelics Teaches Us About Consciousness, Dying, Addiction, Depression, and Transcendence",
        "author": "Michael Pollan",
        "year": 2018,
        "pages": 465,
        "language": "English",
        "rating": 4.5
    },
    {
        "title": "The Structure of Scientific Revolutions",
        "author": "Thomas S. Kuhn",
        "year": 1962,
        "pages": 264,
        "language": "English",
        "rating": 4.0
    },
    {
        "title": "Stiff: The Curious Lives of Human Cadavers",
        "author": "Mary Roach",
        "year": 2003,
        "pages": 303,
        "language": "English",
        "rating": 4.1
    },
    {
        "title": "Why Nations Fail: The Origins of Power, Prosperity, and Poverty",
        "author": "Daron Acemoglu, James A. Robinson",
        "year": 2012,
        "pages": 529,
        "language": "English",
        "rating": 4.1
    }
]


add_books_to_database(books_data)