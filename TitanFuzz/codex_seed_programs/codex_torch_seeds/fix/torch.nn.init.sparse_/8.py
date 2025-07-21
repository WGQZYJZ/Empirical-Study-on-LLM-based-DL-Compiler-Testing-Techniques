'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
torch.nn.init.sparse_(input_data, sparsity=0.5, std=0.1)
print(input_data)