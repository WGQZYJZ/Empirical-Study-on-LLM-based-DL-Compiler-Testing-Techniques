import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(10, 1, dtype=torch.float32, requires_grad=True)
y = torch.clone(x)