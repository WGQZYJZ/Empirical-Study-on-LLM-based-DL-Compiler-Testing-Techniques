'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3)
print(x)
print(torch.neg(x))