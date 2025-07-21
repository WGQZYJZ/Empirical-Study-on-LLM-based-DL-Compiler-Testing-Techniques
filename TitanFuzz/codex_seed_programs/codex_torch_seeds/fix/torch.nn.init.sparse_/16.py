'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
input_data = torch.randn(3, 5)
print('Input data:', input_data)
torch.nn.init.sparse_(input_data, sparsity=0.5)
print('Sparse initialized data:', input_data)