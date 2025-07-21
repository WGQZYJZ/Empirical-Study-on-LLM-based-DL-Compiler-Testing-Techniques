import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 5))
input_data = input_data.requires_grad_()
clip_value = 2
torch.nn.utils.clip_grad_value_(input_data, clip_value)