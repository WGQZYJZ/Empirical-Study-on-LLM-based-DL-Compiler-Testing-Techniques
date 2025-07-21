import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 3)
sampler = torch.utils.data.Sampler(input_data)
batch_sampler = torch.utils.data.BatchSampler(sampler, batch_size=2, drop_last=True)
sequential_sampler = torch.utils.data.SequentialSampler