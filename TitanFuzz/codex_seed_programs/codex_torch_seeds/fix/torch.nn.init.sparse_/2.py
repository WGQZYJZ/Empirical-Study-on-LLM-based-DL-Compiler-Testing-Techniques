'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.sparse_\ntorch.nn.init.sparse_(tensor, sparsity, std=0.01)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.nn.init.sparse_')
tensor = torch.empty(2, 3)
print(tensor)
print('\n')
torch.nn.init.sparse_(tensor, sparsity=0.2, std=0.01)
print(tensor)