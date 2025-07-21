'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
import torch.nn as nn
input_tensor = torch.randn(3, 3)
torch.nn.init.sparse_(input_tensor, sparsity=0.5, std=0.01)
print(input_tensor)