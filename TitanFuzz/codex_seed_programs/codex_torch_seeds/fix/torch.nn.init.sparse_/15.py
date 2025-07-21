'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
import torch
tensor = torch.empty(2, 2)
torch.nn.init.sparse_(tensor, sparsity=0.5)
print(tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
import torch
tensor = torch.empty(2, 2)
torch.nn.init.xavier_normal_(tensor)
print(tensor)