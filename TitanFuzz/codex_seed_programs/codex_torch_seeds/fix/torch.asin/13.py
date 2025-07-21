'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
x = torch.tensor([1.0, 0.0, (- 1.0)])
y = torch.asin(x)
print(y)