import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(10, 5))
torch.nn.init.xavier_uniform_(input_data)
input_data = Variable(torch.randn(10, 5))
torch.nn.init.xavier_normal_(input_data)