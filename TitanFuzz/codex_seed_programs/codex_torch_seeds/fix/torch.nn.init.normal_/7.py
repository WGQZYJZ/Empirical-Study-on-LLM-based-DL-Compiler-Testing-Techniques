'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0.0, std=1.0)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.nn.init.normal_')
print('torch.nn.init.normal_(tensor, mean=0.0, std=1.0)')
x = torch.empty(2, 3)
print('x = torch.empty(2, 3)')
print('torch.nn.init.normal_(x)')
torch.nn.init.normal_(x)
print(x)
print('torch.nn.init.normal_(x, mean=0.5, std=0.1)')
torch.nn.init.normal_(x, mean=0.5, std=0.1)
print(x)