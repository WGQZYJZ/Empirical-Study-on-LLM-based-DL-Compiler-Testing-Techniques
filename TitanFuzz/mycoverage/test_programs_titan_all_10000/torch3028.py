import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([0.2, 0.3, 0.8, 0.6])
output = torch.bernoulli(input)
output = torch.bernoulli(torch.Tensor([0.2]))
input = torch.Tensor([0.2, 0.3, 0.8, 0.6])
output = torch.bernoulli(input)
input = torch.Tensor([0.2, 0.3, 0.8, 0.6])
output = torch.bernoulli(input)