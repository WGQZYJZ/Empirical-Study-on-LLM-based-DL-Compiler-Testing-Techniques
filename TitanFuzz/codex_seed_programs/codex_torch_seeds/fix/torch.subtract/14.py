'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.subtract\ntorch.subtract(input, other, *, alpha=1, out=None)\n'
import torch
x = torch.tensor(3.0)
y = torch.tensor(2.0)
z = torch.subtract(x, y)
print(z)