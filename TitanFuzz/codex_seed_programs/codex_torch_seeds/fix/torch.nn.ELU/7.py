'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
x = torch.randn(1, 1, 3)
print(x)
elu = torch.nn.ELU(alpha=1.0, inplace=False)
print(elu(x))