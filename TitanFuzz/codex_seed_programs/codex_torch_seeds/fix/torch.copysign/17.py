'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.copysign\ntorch.copysign(input, other, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), 2.0, (- 3.0), 4.0])
y = torch.tensor([1.0, (- 2.0), 3.0, (- 4.0)])
z = torch.copysign(x, y)
print(z)