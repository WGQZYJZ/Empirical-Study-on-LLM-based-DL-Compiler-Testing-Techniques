'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
from torch.nn import init
input_data = torch.rand(2, 3)
print(input_data)
init.sparse_(input_data, sparsity=0.5, std=0.01)
print(input_data)