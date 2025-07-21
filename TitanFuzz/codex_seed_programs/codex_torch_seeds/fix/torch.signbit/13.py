'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.signbit\ntorch.signbit(input, *, out=None)\n'
import torch
input = torch.randn(1, 3)
print(input)
signbit = torch.signbit(input)
print(signbit)