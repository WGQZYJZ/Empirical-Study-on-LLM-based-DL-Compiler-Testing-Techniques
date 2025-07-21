'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import torch
x = torch.randn(2, 2)
y = torch.nn.ELU(alpha=1.0, inplace=False)(x)
print(y)