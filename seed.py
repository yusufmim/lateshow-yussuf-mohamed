from models import db, Episode, Guest, Appearance
from datetime import datetime
import pandas as pd

def seed_data():
    db.drop_all()
    db.create_all()

    # Seed Guests from CSV
    guests_df = pd.read_csv('guests.csv')
    for _, row in guests_df.iterrows():
        guest = Guest(id=row['id'], name=row['name'], occupation=row['occupation'])
        db.session.add(guest)

    # Seed Episodes
    episodes = [
        Episode(date="1/11/99", number=1),
        Episode(date="1/12/99", number=2)
    ]
    db.session.bulk_save_objects(episodes)

    # Seed Appearances
    appearances = [
        Appearance(rating=4, episode_id=1, guest_id=1),
        Appearance(rating=5, episode_id=2, guest_id=3)
    ]
    db.session.bulk_save_objects(appearances)

    db.session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    from app import app
    with app.app_context():
        seed_data()