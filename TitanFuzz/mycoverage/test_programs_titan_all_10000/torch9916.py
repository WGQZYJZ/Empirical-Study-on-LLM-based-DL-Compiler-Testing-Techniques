import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
torch.nn.init.xavier_uniform_(input_data)
torch.nn.init.xavier_uniform_(input_data, gain=0.5)