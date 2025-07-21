'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
x = torch.randn(1, 2)
print(x)
selu = torch.nn.SELU()
print(selu(x))