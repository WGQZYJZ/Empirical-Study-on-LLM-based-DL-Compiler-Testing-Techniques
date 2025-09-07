import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, 3, 2, 3, 1, 2, 1, 2, 3, 1, 3, 2])
torch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)
input = torch.tensor([1, 3, 2, 3, 1, 2, 1, 2, 3, 1, 3, 2])