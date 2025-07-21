'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
x = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]])
y = torch.negative(x)
print(y)