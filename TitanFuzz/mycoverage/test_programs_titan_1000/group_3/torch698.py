import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3])
weights = torch.tensor([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
output = torch.bincount(input, weights=weights, minlength=4)