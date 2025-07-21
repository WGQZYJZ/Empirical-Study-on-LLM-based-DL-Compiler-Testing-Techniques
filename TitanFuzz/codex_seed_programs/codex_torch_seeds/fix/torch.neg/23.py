'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.neg\ntorch.neg(input, *, out=None)\n'
import torch
x = torch.rand(2, 3)
print(x)
y = torch.neg(x)
print(y)