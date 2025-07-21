'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
import torch.nn.functional as F
x = torch.randn(2, 2)
print('Input data: ', x)
y = F.celu(x, alpha=1.0, inplace=False)
print('Output data: ', y)