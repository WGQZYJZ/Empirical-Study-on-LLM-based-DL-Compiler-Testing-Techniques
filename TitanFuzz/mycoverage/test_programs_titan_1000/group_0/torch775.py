import torch
from torch import nn
from torch.autograd import Variable
input = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.max(input, dim=0)
torch.max(input, dim=1)
torch.max(input, dim=0, keepdim=True)
torch.max(input, dim=1, keepdim=True)
input = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])