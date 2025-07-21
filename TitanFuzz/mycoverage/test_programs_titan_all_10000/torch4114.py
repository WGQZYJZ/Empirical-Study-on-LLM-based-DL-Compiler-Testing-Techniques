import torch
from torch import nn
from torch.autograd import Variable
x = np.random.randn(100, 3, 32, 32)
y = np.random.randn(100)
sampler = torch.utils.data.SequentialSampler(range(len(x)))
batch_sampler = torch.utils.data.BatchSampler(sampler, batch_size=2, drop_last=False)
for indices in batch_sampler:
    print(indices)