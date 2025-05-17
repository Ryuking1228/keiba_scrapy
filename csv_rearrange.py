import pandas as pd


def rearrange():
    name = pd.read_csv('name.csv', header=None)
    gen_born = pd.read_csv('gen_born.csv', header=None)
    others = pd.read_csv('others.csv', header=None)

    gen = gen_born.iloc[::2].reset_index(drop=True)
    born = gen_born.iloc[1::2].reset_index(drop=True)[0].str.extract('>(.*)<', expand=False)

    uma_house = others.iloc[1::7].reset_index(drop=True)
    father = others.iloc[2::7].reset_index(drop=True)
    mother = others.iloc[3::7].reset_index(drop=True)
    mother_father = others.iloc[4::7].reset_index(drop=True)
    uma_owner = others.iloc[5::7].reset_index(drop=True)
    producer = others.iloc[6::7].reset_index(drop=True)

    df = pd.concat([
        name,
        gen,
        born,
        uma_house,
        father,
        mother,
        mother_father,
        uma_owner,
        producer,
    ], axis=1)

    df.to_csv('result.csv', index=False, header=False)


def main():
    rearrange()


if __name__ == '__main__':
    main()
