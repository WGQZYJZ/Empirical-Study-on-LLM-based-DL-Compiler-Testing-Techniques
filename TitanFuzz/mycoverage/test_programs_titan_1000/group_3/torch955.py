import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 1, 1, 2, 2, 3, 3, 3, 3, 3]])
output = torch.unique_consecutive(input, return_inverse=True, return_counts=True)