import torch
from torch import nn
from torch.autograd import Variable
input_size = 10
output_size = 20
input = torch.rand(input_size, output_size)
torch.nn.init.xavier_uniform_(input)