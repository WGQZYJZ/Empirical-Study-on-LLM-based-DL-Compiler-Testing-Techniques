import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 1, 3, 3))
torch.nn.utils.parametrize.cached()