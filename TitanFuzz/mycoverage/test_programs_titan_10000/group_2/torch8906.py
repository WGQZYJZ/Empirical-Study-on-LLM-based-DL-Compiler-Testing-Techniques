import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(2, 3)
x = torch.nn.GELU()(input_data)