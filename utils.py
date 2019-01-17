import csv


class Terms:
    start_tokens = ('@', '<', '`')

    @classmethod
    def get_terminologies(cls, text):
        terms = []
        for word in text.split(' '):
            if word[0] in cls.start_tokens:
                terms.append(word)
        return terms

    def save_new_terms(self, text):
        terms = self.get_terminologies(text)
        current_terms = []
        with open('./terminologies.csv', 'r') as terms_file:
            csv_reader = csv.DictReader(terms_file, delimiter=',')
            current_terms = [row['en'] for row in csv_reader]
        new_terms = set(terms) - set(current_terms)
        with open('./terminologies.csv', 'a', newline='') as terms_file:
            csv_writer = csv.writer(terms_file)
            for term in new_terms:
                csv_writer.writerow([term, term])


terms = Terms()
