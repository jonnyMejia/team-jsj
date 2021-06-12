from .sprint1 import (remove_accents, 
                           remove_punctuation_space_end, 
                           remove_punctuation_space_start, 
                           delete_arroba_unicode, 
                           remove_tags_html)

def clearDataset(dataset, name):

    return dataset[name].apply(remove_accents).apply(remove_punctuation_space_start).apply(
            remove_punctuation_space_end).apply(lambda s:s.upper())