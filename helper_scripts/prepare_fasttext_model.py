import gzip
import shutil


def prep_embedding_model():
    ft_path = 'cc.en.300.bin.gz'
    with gzip.open(ft_path, 'rb') as f_in:
        with open('cc.en.300.bin', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


if __name__ == '__main__':
    prep_embedding_model()
