import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(4, 4)
torch.nn.init.sparse_(input_data, sparsity=0.5)
torch.nn.init.sparse_(input_data, sparsity=0.5, std=0.01)