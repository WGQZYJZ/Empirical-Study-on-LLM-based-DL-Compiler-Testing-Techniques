'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
data = torch.randn(5, 5)
print(data)
print(torch.sign(data))