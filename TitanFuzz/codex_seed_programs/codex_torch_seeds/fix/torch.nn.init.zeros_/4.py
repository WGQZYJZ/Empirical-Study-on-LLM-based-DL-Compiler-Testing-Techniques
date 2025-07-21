'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
from torch.nn import init
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.nn.init.zeros_')
tensor = torch.ones(2, 3)
print('tensor:', tensor)
init.zeros_(tensor)
print('tensor:', tensor)