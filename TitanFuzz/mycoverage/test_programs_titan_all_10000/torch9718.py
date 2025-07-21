import torch
from torch import nn
from torch.autograd import Variable
input_size = 5
output_size = 2
input = torch.randn(input_size, output_size)
torch.nn.init.xavier_normal_(input)
input_size = 5
output_size = 2
input = torch.randn(input_size, output_size)
torch.nn.init.xavier_uniform_(input)