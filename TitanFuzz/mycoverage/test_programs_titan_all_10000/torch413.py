import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, 3, 2, 3])
result = torch.unique(input)
result = torch.unique(input, sorted=True, return_inverse=True, return_counts=True)