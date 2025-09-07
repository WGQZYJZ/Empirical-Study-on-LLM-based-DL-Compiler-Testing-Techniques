import torch
from torch import nn
from torch.autograd import Variable

data = torch.arange(0, 10)
batch_sampler = torch.utils.data.BatchSampler(torch.utils.data.sampler.SequentialSampler(data), batch_size=3, drop_last=False)
for batch in batch_sampler:
    print(batch)