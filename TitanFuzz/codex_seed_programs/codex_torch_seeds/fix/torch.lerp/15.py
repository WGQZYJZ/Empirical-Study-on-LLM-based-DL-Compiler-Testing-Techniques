'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
c = torch.lerp(a, b, 0.5)
print(c)