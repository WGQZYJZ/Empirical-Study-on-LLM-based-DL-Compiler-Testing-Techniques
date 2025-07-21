import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[1, 1, 1, 1], [0, 0, 0, 0]])
torch.any(input, dim=0)
torch.any(input, dim=1)
torch.any(input, dim=1, keepdim=True)
torch.any(input, dim=(- 1), keepdim=True)
torch.any(input, dim=(- 1), keepdim=False)
torch.any(input, dim=0, keepdim=True)