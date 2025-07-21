'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
'\nTask 1: import PyTorch\n'
import torch
'\nTask 2: Generate input data\n'
x = torch.rand(1)
print('x = ', x)
'\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
torch.random.manual_seed(1)
x = torch.rand(1)
print('x = ', x)