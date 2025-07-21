'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0.0, std=1.0)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.nn.init.normal_')
tensor = torch.empty(2, 3)
print('torch.nn.init.normal_(tensor, mean=0.0, std=1.0)')
torch.nn.init.normal_(tensor, mean=0.0, std=1.0)
print('tensor =', tensor)