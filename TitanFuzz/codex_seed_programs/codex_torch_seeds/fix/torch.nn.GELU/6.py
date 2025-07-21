'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
x = torch.randn(1, 1, 3, 3)
print(x)
y = torch.nn.GELU()(x)
print(y)