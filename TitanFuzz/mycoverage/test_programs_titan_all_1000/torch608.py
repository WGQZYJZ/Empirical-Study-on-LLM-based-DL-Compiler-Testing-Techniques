import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 100)
batch_sampler = torch.utils.data.BatchSampler(sampler=torch.utils.data.SequentialSampler(data), batch_size=10, drop_last=True)
for batch_indices in batch_sampler:
    print(batch_indices)