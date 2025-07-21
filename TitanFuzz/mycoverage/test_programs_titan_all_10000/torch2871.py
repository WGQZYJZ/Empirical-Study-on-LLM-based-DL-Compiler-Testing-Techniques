import torch
from torch import nn
from torch.autograd import Variable
data = torch.rand(10)
sampler = torch.utils.data.BatchSampler(data, batch_size=3, drop_last=True)
for i in sampler:
    print(i)