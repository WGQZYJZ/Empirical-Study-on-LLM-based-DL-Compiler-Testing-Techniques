import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1, 2, 3, 4])
other = torch.tensor([5, 6, 7, 8])
output = torch.dot(input, other)