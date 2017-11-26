class CollatzSeq():
    def __init__(self, start_value):
        self.start_value = start_value
        self.sequence = [self.start_value, ]

        if not isinstance(self.start_value, int) or self.start_value < 1:
            raise ValueError

        self.count_seq()

    def count_seq(self):

        first_num = self.start_value
        while self.sequence[-1] != 1:
            if first_num % 2 == 0:
                next_num = first_num // 2
                self.sequence.append(next_num)
                first_num = next_num

            elif first_num % 2 != 0:
                next_num = 3 * first_num + 1
                self.sequence.append(next_num)
                first_num = next_num
        return self.sequence

    def __getitem__(self, index):
        return self.sequence[index]

    def __len__(self):
        return len(self.sequence)


def longest_collatz(start, stop):
    longest_seq = 0
    x = 0
    for i in range(start, stop):
        seq = CollatzSeq(i)
        if len(seq) > longest_seq:
            longest_seq = len(seq)
            x = i
    return longest_seq, x
