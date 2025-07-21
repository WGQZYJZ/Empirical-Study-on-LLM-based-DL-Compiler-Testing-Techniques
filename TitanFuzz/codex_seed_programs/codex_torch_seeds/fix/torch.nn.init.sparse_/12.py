'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
import torch
data = torch.rand(4, 4)
torch.nn.init.sparse_(data, sparsity=0.5, std=0.01)
print(data)