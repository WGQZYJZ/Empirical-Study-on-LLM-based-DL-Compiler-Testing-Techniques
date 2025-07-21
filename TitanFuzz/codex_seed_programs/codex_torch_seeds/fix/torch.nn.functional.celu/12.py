'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
x = torch.randn(3, 3)
print('Input data: ', x)
y = torch.nn.functional.celu(x)
print('Output data: ', y)