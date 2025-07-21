'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
x = torch.rand(1, requires_grad=True)
print(x)
print(torch.signbit(x))