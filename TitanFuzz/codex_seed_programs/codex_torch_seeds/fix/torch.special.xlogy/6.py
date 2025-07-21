'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.xlogy\ntorch.special.xlogy(input, other, *, out=None)\n'
import torch
x = torch.tensor([(- 1), 0, 1, 2])
y = torch.tensor([(- 1), 1, 1, 2])
print(torch.special.xlogy(x, y))