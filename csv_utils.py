import pandas as pd

def csv_sampler(header, conditions, results_idx=None, template='Plain', svPath=None):
    d = dict.fromkeys(header)

    if template == 'Plain':
        pass
        # conditions sorted by header
        # in data area, display each condition combination once
        # followed by a row of ...'s
        # define different types of templates. not sure exactly what this means at this moment


    if results_idx is not None:
        pass
        # idx of column that begins contain data, opposed to conditions/meta info

    df = pd.DataFrame(data=d)
    if svPath is None:
        pass
        # save to desktop or some default folder "csv_templates"
    else:
        pass
        # path should be specified by user
    
    df.to_csv(svPath, index=False)
