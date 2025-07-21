'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
import torch
input_tensor = torch.randn(3, 5)
torch.nn.init.orthogonal_(input_tensor)
print(input_tensor)
import torch
input_tensor = torch.randn(3, 5)
torch.nn.init.orthogonal_(input_tensor, gain=2)
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch