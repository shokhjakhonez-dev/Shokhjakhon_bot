import aiosqlite

DB_NAME = "lab.db"

async def create_tables():
    async with aiosqlite.connect(DB_NAME) as db:

        # Doktorlar
        await db.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            phone TEXT,
            clinic TEXT
        )
        """)

        # Shogirtlar
        await db.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            phone TEXT
        )
        """)

        # Ishlar
        await db.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_id INTEGER,
            patient TEXT,
            job_type TEXT,
            price INTEGER,
            paid INTEGER DEFAULT 0,
            debt INTEGER DEFAULT 0,
            status TEXT,
            created_at TEXT
        )
        """)

        # To'lovlar
        await db.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER,
            amount INTEGER,
            payment_date TEXT
        )
        """)
# Ishlar
await db.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor TEXT,
    student TEXT,
    patient TEXT,
    work TEXT,
    price INTEGER,
    paid INTEGER DEFAULT 0,
    status TEXT DEFAULT 'Yangi',
    deadline TEXT,
    note TEXT
)
""")
        await db.commit()
