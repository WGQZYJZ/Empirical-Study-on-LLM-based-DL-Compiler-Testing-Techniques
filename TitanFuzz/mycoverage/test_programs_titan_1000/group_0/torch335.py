import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(10, 10)
y = torch.rand(10, 10)
torch.nn.utils.clip_grad_value_(x, 2)
x = torch.rand(10, 10)
y = torch.rand(10, 10)
torch.nn.utils.clip_grad_norm_(x, 1)