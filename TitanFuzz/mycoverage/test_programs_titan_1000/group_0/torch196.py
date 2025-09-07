import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, requires_grad=True)
torch.nn.init.sparse_(input_data, sparsity=0.5)