import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mode = torch.mode(input, dim=(- 1), keepdim=False, out=None)
mode = torch.mode(input, dim=(- 1), keepdim=True, out=None)
mode = torch.mode(input, dim=0, keepdim=False, out=None)
mode = torch.mode(input, dim=0, keepdim=True, out=None)
mode = torch.mode(input, dim=1, keepdim=False, out=None)
mode = torch.mode(input, dim=1, keepdim=True, out=None)