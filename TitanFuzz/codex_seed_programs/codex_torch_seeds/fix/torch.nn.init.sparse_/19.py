'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
import numpy as np
from torch import nn
from torch.nn import init
from torch.autograd import Variable
input_size = 10
batch_size = 16
hidden_size = 128
num_classes = 10
tensor = torch.randn(input_size, hidden_size)
print(tensor)
tensor = init.sparse_(tensor, sparsity=0.5, std=0.01)
print(tensor)