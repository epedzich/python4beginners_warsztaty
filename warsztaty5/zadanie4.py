import requests


def sw_person_generator():
    url = 'https://swapi.co/api/people/'
    while url:
        try:
            r = requests.get(url)
        except requests.ConnectionError:
            return
        x = r.json()
        url = x['next']
        for person in x['results']:
            yield person['name']




if __name__ == '__main__':
    l = set(sw_person_generator())
    expected = {'Luke Skywalker', 'C-3PO', 'R2-D2', 'Darth Vader', 'Leia Organa', 'Owen Lars', 'Beru Whitesun lars',
                'R5-D4', 'Biggs Darklighter', 'Obi-Wan Kenobi', 'Anakin Skywalker', 'Wilhuff Tarkin', 'Chewbacca',
                'Han Solo', 'Greedo', 'Jabba Desilijic Tiure', 'Wedge Antilles', 'Jek Tono Porkins', 'Yoda',
                'Palpatine',
                'Boba Fett', 'IG-88', 'Bossk', 'Lando Calrissian', 'Lobot', 'Ackbar', 'Mon Mothma', 'Arvel Crynyd',
                'Wicket Systri Warrick', 'Nien Nunb', 'Qui-Gon Jinn', 'Nute Gunray', 'Finis Valorum', 'Padmé Amidala',
                'Jar Jar Binks', 'Roos Tarpals', 'Rugor Nass', 'Ric Olié', 'Watto', 'Sebulba', 'Quarsh Panaka',
                'Shmi Skywalker', 'Darth Maul', 'Bib Fortuna', 'Ayla Secura', 'Ratts Tyerell', 'Dud Bolt', 'Gasgano',
                'Ben Quadinaros', 'Mace Windu', 'Ki-Adi-Mundi', 'Kit Fisto', 'Eeth Koth', 'Adi Gallia', 'Saesee Tiin',
                'Yarael Poof', 'Plo Koon', 'Mas Amedda', 'Gregar Typho', 'Cordé', 'Cliegg Lars', 'Poggle the Lesser',
                'Luminara Unduli', 'Barriss Offee', 'Dormé', 'Dooku', 'Bail Prestor Organa', 'Jango Fett', 'Zam Wesell',
                'Dexter Jettster', 'Lama Su', 'Taun We', 'Jocasta Nu', 'R4-P17', 'Wat Tambor', 'San Hill', 'Shaak Ti',
                'Grievous', 'Tarfful', 'Raymus Antilles', 'Sly Moore', 'Tion Medon', 'Finn', 'Rey', 'Poe Dameron',
                'BB8',
                'Captain Phasma'}
    assert l == expected
