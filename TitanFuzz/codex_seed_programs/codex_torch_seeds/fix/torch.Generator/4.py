"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Generator\ntorch.Generator(device='cpu')\n"
import torch
x = torch.rand(3, 3)
print(x)
g = torch.Generator(device='cpu')
print(g)