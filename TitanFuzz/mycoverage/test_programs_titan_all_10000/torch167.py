import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[3, 6], [2, 4]])
other = torch.tensor([[2, 2], [3, 9]])
torch.lcm(input, other, out=None)
input = torch.tensor([[1, 2], [3, 4]])
torch.log(input, out=None)