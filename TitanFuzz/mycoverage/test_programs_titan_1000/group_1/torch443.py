import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
torch.nn.init.uniform_(input_data, a=0.0, b=1.0)
torch.nn.init.normal_(input_data, mean=0.0, std=1.0)