import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.empty(3, 5)
torch.nn.init.sparse_(input_tensor, sparsity=0.5, std=0.01)