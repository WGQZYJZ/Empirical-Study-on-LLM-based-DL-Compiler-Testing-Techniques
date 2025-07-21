import torch
from torch import nn
from torch.autograd import Variable
data = np.arange(20)
sampler = torch.utils.data.SubsetRandomSampler(indices=[1, 3, 5, 7, 9])
for (i, index) in enumerate(sampler):
    print('index: {} data: {}'.format(index, data[index]))