import torch
from torch import nn
from torch.autograd import Variable
input_size = 10
x = torch.empty(input_size, requires_grad=True)
torch.nn.init.normal_(x)