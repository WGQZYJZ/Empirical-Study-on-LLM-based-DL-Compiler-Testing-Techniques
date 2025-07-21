import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)
torch.nn.utils.clip_grad_value_(y, 0.5)