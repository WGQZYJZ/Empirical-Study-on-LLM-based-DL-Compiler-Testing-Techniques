import torch
from torch import nn
from torch.autograd import Variable

a = torch.randn(2, 2)
torch.Tensor.get_device(a)