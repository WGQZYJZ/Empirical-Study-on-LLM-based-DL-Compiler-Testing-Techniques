import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(2, 3, 4)
swap_data = torch.swapaxes(data, 0, 2)