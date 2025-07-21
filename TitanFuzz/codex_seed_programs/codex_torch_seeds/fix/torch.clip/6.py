'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clip\ntorch.clip(input, min=None, max=None, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), 1.0, (- 0.5), 0.5])
y = torch.clip(x, (- 0.5), 0.5)
print(y)