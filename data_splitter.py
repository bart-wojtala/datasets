import os
import random
import linecache


def split_data(csv_file, train_set_size):
    records = get_file_len(csv_file)
    val_size = round((1 - train_set_size) * records)
    val_lines = get_random_lines(csv_file, records, val_size)
    print("Total dataset size: " + str(records))
    print("Validation set size: " + str(val_size))
    full_dataset = get_all_lines(csv_file, records)
    train_lines = [l for l in full_dataset if l not in val_lines]

    with open('dataset_val.txt', "w") as f:
        for line in val_lines:
            f.write(f'{line}')
    with open('dataset_train.txt', "w") as f:
        for line in train_lines:
            f.write(f'{line}')


def get_file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_random_lines(filename, dataset_size, val_size):
    idxs = random.sample(range(dataset_size), val_size)
    return [linecache.getline(filename, i) for i in idxs]


def get_all_lines(filename, dataset_size):
    with open(filename) as f:
        return f.readlines()


if __name__ == "__main__":
    split_data("datasets/trump/metadata.csv", 0.9)
