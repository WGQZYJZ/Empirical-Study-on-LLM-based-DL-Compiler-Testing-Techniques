'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i1e\ntorch.special.i1e(input, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = torch.special.i1e(x)
print(y)
y = torch.special.i1e(x, out=torch.empty(x.shape))
print(y)