import torch
from torch import nn
from torch.autograd import Variable
input_size = (3, 3)
sparsity = 0.5
input_data = torch.randn(input_size)
torch.nn.init.sparse_(input_data, sparsity)