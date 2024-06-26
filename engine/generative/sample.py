import random
from n_array import NArray


class Sample:
    def creator(N):
        """
        This is the real data creator
        ___

        Generate (N2+1)x(N2+1) original patterns
        Like the one below
        - - - - - + - - - - -
        - - - - + - + - - - -
        - - - + - - - + - - -
        - - + - - - - - + - -
        - + - - - - - - - + -
        + - - - - - - - - - +
        - + - - - - - - - + -
        - - + - - - - - + - -
        - - - + - - - + - - -
        - - - - + - + - - - -
        - - - - - + - - - - -
        """
        D = N + 1
        sample = NArray.n2(D)
        x, y = 0, D - 1
        while x < D:
            sample[y][x] = 1
            x += random.choice([0, 1])
            y -= random.choice([0, 1])
            if y < 0:
                y = 0
        sample = NArray.unfold(sample)
        if random.choice([0, 1]) == 1:
            sample = NArray.rotate90(sample)
        return sample

    def creator2(N):
        """
        This is the real data creator
        ___

        Generate (N2+1)x(N2+1) original patterns
        Like the one below
        - - - - - + - - - - -
        - - - - + - + - - - -
        - - - + - - - + - - -
        - - + - - - - - + - -
        - + - - - - - - - + -
        + - - - - - - - - - +
        - + - - - - - - - + -
        - - + - - - - - + - -
        - - - + - - - + - - -
        - - - - + - + - - - -
        - - - - - + - - - - -
        """
        D = N + 1
        sample = NArray.n2(D)
        x, y = random.randrange(0, N), random.randrange(0, N)
        xd, yd = random.choice([-1, 1]), random.choice([-1, 1])
        while x < random.randrange(N, N * 2):
            sample[y][x] = 1
            if random.random() > 0.7:
                xd, yd = random.choice([-1, 1]), random.choice([-1, 1])
            x += xd
            y += yd
            if x < 0:
                x = 0
            if x > N:
                x = N
            if y < 0:
                y = 0
            if y > N:
                y = N
        sample = NArray.unfold(sample)
        if random.choice([0, 1]) == 1:
            sample = NArray.rotate90(sample)
        return sample

    def generator(N):
        """
        This is the fake data generator
        FIXME: this should be NN
        """
        D = N + 1
        sample = NArray.n2(D)
        for _ in range(D * 2):
            x = random.randrange(0, D)
            y = random.randrange(0, D)
            sample[x][y] = 1
        sample = NArray.unfold(sample)
        if random.choice([0, 1]) == 1:
            sample = NArray.rotate90(sample)
        return sample

    def discriminator(sample):
        """
        This is the investigator
        FIXME: this should be NN
        """

        E = 1  # Error

        def get_max_score(sample):
            score = 0
            for row in sample:
                for cel in row:
                    if cel == 1:
                        score += 1
            return score

        max_score = get_max_score(sample)
        score = max_score

        def getCell(x, y):
            try:
                pos = sample[x][y]
            except:
                pos = 0
            return pos

        for r in range(0, len(sample)):
            for c in range(0, len(sample[0])):
                c1 = sample[r][c]

                checks = (
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                    (r - 1, c - 1),
                    (r - 1, c + 1),
                    (r + 1, c - 1),
                    (r + 1, c + 1),
                )
                found = False
                for check in checks:
                    found = found or getCell(check[0], check[1]) == 1

                if c1 == 1 and not found:
                    score -= 1
        return (max_score - (max_score * E / 100) <= score, max_score, score)
