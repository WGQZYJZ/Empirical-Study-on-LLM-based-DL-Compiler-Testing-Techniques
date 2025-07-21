'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
input = torch.randn(4)
print(input)
other = torch.randint(3, (4,), dtype=torch.int32)
print(other)
out = torch.ldexp(input, other)
print(out)