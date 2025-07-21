'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
input_size = (3, 3)
sparsity = 0.5
input_data = torch.randn(input_size)
print(input_data)
torch.nn.init.sparse_(input_data, sparsity)
print(input_data)