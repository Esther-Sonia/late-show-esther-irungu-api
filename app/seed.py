import random
import csv
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Episode, Guest, Appearance

app = create_app()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        episode_number = 1  

        with open('guests.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    date = row['Show'].strip()
                    occupation = row['GoogleKnowledge_Occupation'].strip()
                    raw_guest_list = row['Raw_Guest_List'].strip()

                    guest_names = [name.strip() for name in raw_guest_list.split(',') if name.strip() and name.strip() != 'NA']

                    if not date or not guest_names:
                        continue  

                    episode = Episode.query.filter_by(date=date).first()
                    if not episode:
                        episode = Episode(date=date, number=episode_number)
                        db.session.add(episode)
                        db.session.commit()
                        episode_number += 1

                    for name in guest_names:
                        guest = Guest.query.filter_by(name=name).first()
                        if not guest:
                            guest = Guest(name=name, occupation=occupation)
                            db.session.add(guest)
                            db.session.commit()

                        appearance = Appearance(
                            guest_id=guest.id,
                            episode_id=episode.id,
                            rating=random.randint(1, 5)
                        )
                        db.session.add(appearance)

                except KeyError as e:
                    print(f"Skipping row due to missing column: {e}")
                except Exception as e:
                    print(f" Error processing row: {e}")

        db.session.commit()
        print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()
