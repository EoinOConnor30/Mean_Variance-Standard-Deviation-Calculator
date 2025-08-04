import numpy as np
np.set_printoptions(legacy='1.25')

def calculate(list):
    if len(list)<9:
        raise ValueError('List must contain nine numbers.')
    else:
        list2 = np.reshape(list, (3,3))
        calculations = {
                     'mean':[np.mean(list2, axis=0).tolist(), np.mean(list2, axis=1).tolist(), np.mean(list2)],
                     'variance':[np.var(list2, axis=0).tolist(), np.var(list2, axis=1).tolist(), np.var(list2)],
                     'standard deviation':[np.std(list2, axis=0).tolist(), np.std(list2, axis=1).tolist(), np.std(list2)],
                     'max':[np.max(list2, axis=0).tolist(), np.max(list2, axis=1).tolist(), np.max(list2)],
                     'min':[np.min(list2, axis=0).tolist(), np.min(list2, axis=1).tolist(), np.min(list2)],
                     'sum':[np.sum(list2, axis=0).tolist(), np.sum(list2, axis=1).tolist(), np.sum(list2)]
        }
                    
    return calculations