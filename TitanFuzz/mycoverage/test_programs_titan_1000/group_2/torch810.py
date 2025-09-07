import torch
from torch import nn
from torch.autograd import Variable
mean = torch.tensor(0.0)
std = torch.tensor(1.0)
size = torch.Size([3, 3])
torch.normal(mean, std, size)
torch.normal(mean, std, size, out=None)