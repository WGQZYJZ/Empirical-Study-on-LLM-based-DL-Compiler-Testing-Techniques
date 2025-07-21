'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
print(torch.ldexp(a, b))
print(torch.lerp(a, b, 0.5))
print(torch.log(a))
print(torch.log10(a))
print(torch.log1p(a))
print(torch.log2(a))