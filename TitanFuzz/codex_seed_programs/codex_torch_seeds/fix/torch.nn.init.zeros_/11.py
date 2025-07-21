'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
x = torch.randn(2, 3)
print('x = ', x)
torch.nn.init.zeros_(x)
print('x = ', x)