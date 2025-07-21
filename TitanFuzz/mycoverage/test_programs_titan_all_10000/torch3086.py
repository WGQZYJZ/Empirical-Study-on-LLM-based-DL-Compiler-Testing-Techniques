import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(10)
batch_size = 3
batch_sampler = torch.utils.data.BatchSampler(input_data, batch_size, drop_last=False)
for i in batch_sampler:
    print(i)