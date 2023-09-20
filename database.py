from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///courses.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

Base = declarative_base()

class FileInfo(Base):
    __tablename__ = 'organize_me'

    id = Column(Integer, primary_key=True)
    root_name = Column(String, nullable=False)
    folder = Column(String, nullable=False)
    file = Column(String, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def add_entry_to_db(root_folder, folder_name, filename):
    session = Session()
    entry = FileInfo(root_name=root_folder, folder=folder_name, file=filename)
    session.add(entry)
    session.commit()
    session.close()

def display_entries():
    session = Session()
    entries = session.query(FileInfo).all()
    for entry in entries:
        print(f"Course: {entry.root_name}, Folder: {entry.folder}, File: {entry.file}")
    session.close()

def search_entries(keyword):
    session = Session()

    keywords = [k.strip() for k in keyword.split(",")]
    query = session.query(FileInfo)

    for keyword in keywords:
        query = query.filter(
            (FileInfo.root_name.ilike(f"%{keyword}%")) |
            (FileInfo.folder.ilike(f"%{keyword}%"))
        )

    entries = query.all()

    if len(entries) == 0:
        print("No data found with your keywords")
    else:
        for entry in entries:
            print(f"Course: {entry.root_name}, Folder: {entry.folder}, File: {entry.file}")
    
    session.close()
