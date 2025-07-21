import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3))
torch.nn.utils.parametrize.is_parametrized(input_data)