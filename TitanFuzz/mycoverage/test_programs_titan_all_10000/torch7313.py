import torch
from torch import nn
from torch.autograd import Variable
data_size = 100
data = torch.rand(data_size)
batch_size = 10
batch_sampler = torch.utils.data.BatchSampler(torch.utils.data.sampler.SubsetRandomSampler(range(data_size)), batch_size=batch_size, drop_last=False)
for (i, batch_indices) in enumerate(batch_sampler):
    print('batch_indices:', batch_indices)
    print('data[batch_indices]:', data[batch_indices])
    print(('-' * 20))