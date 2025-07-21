import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(0, 9)
sampler = torch.utils.data.SequentialSampler(input_data)
for i in sampler:
    print(i)