import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4)
mean_x = torch.mean(x, dim=1, keepdim=True)
mean_x = torch.mean(x, dim=1, keepdim=False)
mean_x = torch.mean(x, dim=0, keepdim=True)
mean_x = torch.mean(x, dim=0, keepdim=False)
mean_x = torch.mean(x, dim=2, keepdim=True)
mean_x = torch.mean(x, dim=2, keepdim=False)