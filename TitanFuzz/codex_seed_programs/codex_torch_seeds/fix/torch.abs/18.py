'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1), (- 2), 3], dtype=torch.float32)
print(x)
y = torch.abs(x)
print(y)