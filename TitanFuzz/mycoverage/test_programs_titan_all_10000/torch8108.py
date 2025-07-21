import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_x = torch.nansum(x, dim=1)
sum_x = torch.nansum(x, dim=1, keepdim=True)