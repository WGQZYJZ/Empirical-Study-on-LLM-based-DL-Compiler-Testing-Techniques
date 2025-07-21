'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trace\ntorch.trace(input)\n'
import torch
x = torch.rand(3, 3)
print(x)
print(torch.trace(x))