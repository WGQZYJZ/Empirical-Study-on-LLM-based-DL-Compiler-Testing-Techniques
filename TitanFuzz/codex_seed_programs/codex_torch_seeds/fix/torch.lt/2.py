'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lt\ntorch.lt(input, other, *, out=None)\n'
import torch
x = torch.tensor([(- 1), 0, 1, 2])
y = torch.tensor([(- 2), 0, 1, 2])
out = torch.lt(x, y)
print(out)