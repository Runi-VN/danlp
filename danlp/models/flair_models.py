from danlp.download import download_model, DEFAULT_CACHE_DIR, _unzip_process_func


def load_flair_ner_model(cache_dir=DEFAULT_CACHE_DIR, verbose=False):
    """

    :param cache_dir:
    :param verbose:
    :return:
    """
    from flair.models import SequenceTagger

    model_weight_path = download_model('flair.ner', cache_dir, process_func=_unzip_process_func, verbose=verbose)

    # using the flair model
    flair_model = SequenceTagger.load(model_weight_path)

    return flair_model

def load_flair_pos_model(cache_dir=DEFAULT_CACHE_DIR, verbose=False):
    """

    :param cache_dir:
    :param verbose:
    :return:
    """
    from flair.models import SequenceTagger

    model_weight_path = download_model('flair.pos', cache_dir, process_func=_unzip_process_func, verbose=verbose)

    # using the flair model
    flair_model = SequenceTagger.load(model_weight_path)

    return flair_model