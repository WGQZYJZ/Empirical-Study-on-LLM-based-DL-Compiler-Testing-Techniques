'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i1e\ntorch.special.i1e(input, *, out=None)\n'
import torch
x = torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = torch.special.i1e(x)
print('input: ', x)
print('output: ', y)