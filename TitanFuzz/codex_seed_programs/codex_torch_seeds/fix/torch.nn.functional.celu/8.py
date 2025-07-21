'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
import torch
x = torch.randn(2, 3)
y = torch.nn.functional.celu(x)
print('x: ', x)
print('y: ', y)