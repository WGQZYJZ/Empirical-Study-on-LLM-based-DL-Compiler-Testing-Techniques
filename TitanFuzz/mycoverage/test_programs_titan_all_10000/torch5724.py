import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = torch.narrow(input, 1, 1, 2)