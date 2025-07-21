import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(10)
sampler = torch.utils.data.SequentialSampler(data)
for i in sampler:
    print('i = ', i)
sampler = torch.utils.data.RandomSampler(data)
for i in sampler:
    print('i = ', i)
indices = torch.LongTensor([0, 2, 4, 6, 8])
sampler = torch.utils.data.SubsetRandomSampler(indices)
for i in sampler:
    print('i = ', i)