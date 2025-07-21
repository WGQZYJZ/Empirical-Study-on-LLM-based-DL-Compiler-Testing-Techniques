import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 100)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.RandomSampler(data), batch_size=5, drop_last=False)
for (i, indices) in enumerate(batch_sampler):
    print(i, indices)