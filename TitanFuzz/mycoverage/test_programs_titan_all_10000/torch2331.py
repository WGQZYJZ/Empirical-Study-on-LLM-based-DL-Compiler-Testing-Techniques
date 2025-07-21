import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(5, 5)
y = torch.nn.functional.selu(x)
y = torch.nn.functional.selu(x, inplace=True)
y = torch.nn.functional.selu(x)