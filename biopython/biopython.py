import logging

proteins = dict()


def count_mass(sequence: str):
    return 4


def count_spectre(sequence: str):
    return [letter for letter in sequence]


class Protein(object):
    sequence = ''
    mass = 0
    spectre = []

    def __init__(self, sequence: str):
        """
        Инициализация нового белка по последовательности.
        :param sequence:
        """
        self.sequence = sequence

        self.mass = count_mass(sequence)
        self.spectre = count_spectre(sequence)

        logging.warning('new protein: ' + sequence)

    def __str__(self):
        """
        Строковое представление белка.
        :return:
        """

        spectre_str = ','.join([str(item) for item in self.spectre])

        return f'mass: {self.mass}, spectre: {spectre_str}, sequence: {self.sequence}'

    @staticmethod
    def get_protein(sequence: str):
        if sequence in proteins:
            print('нашли')
            return proteins[sequence]

        else:
            print('не нашли')
            # создали
            new_protein = Protein(sequence)
            # запомнили
            proteins.update({sequence: new_protein})
            # вернули
            return new_protein


def main():
    a = Protein.get_protein('PRTN')
    b = Protein.get_protein('BLK')
    c = Protein.get_protein('PRTN')
    pass

    print(Protein.get_protein('BLK').spectre)
    print(Protein.get_protein('NEWPRTN').spectre)
    print(c)
    print()
    print(proteins)


if __name__ == '__main__':
    main()
