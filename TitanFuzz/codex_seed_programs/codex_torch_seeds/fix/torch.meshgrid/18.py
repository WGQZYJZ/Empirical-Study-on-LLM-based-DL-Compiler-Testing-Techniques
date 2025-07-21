'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
x = torch.linspace((- 10), 10, 3)
y = torch.linspace((- 10), 10, 4)
(xx, yy) = torch.meshgrid([x, y])
print(xx)
print(yy)