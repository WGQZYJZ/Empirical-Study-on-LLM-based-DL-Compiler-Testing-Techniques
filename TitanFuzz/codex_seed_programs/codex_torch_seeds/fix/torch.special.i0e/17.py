'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0e\ntorch.special.i0e(input, *, out=None)\n'
import torch
x = torch.Tensor([1, 2, 3])
print(x)
y = torch.special.i0e(x)
print(y)