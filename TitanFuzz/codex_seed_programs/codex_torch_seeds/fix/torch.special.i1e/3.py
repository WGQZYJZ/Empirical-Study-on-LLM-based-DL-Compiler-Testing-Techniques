'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i1e\ntorch.special.i1e(input, *, out=None)\n'
import torch
x = torch.randn(10)
y = torch.randn(10)
print('\n i0e \n')
print(torch.special.i0e(x))
print(torch.special.i0e(x, out=y))
print(y)
print('\n i1e \n')
print(torch.special.i1e(x))
print(torch.special.i1e(x, out=y))
print(y)