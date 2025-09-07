import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(3, 2)
torch.set_default_dtype(torch.float64)
x = torch.rand(3, 2)