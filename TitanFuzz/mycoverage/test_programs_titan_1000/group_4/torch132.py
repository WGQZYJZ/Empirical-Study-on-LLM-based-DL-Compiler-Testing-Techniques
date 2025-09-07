import torch
from torch import nn
from torch.autograd import Variable
input_size = 10
output_size = 5
input_data = torch.randn(size=(input_size, output_size))
torch.nn.init.xavier_uniform_(input_data)