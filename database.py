from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///courses.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

Base = declarative_base()

class CourseInfo(Base):
    __tablename__ = 'courseinfo'

    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    folder = Column(String, nullable=False)
    files = Column(String, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def add_entry_to_db(root_folder, folder_name, filename):
    session = Session()
    entry = CourseInfo(course_name=root_folder, folder=folder_name, files=filename)
    session.add(entry)
    session.commit()
    session.close()

def display_entries():
    session = Session()
    entries = session.query(CourseInfo).all()
    for entry in entries:
        print(f"Course: {entry.course_name}, Folder: {entry.folder}, File: {entry.files}")
    session.close()
