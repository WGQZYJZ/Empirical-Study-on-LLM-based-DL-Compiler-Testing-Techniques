'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.normalize\ntorch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)\n'
import torch
import torch.nn.functional as F
x = torch.randn(3, 4)
print('Input data:', x)
normalized_x = F.normalize(x, p=2, dim=1, eps=1e-12)
print('Output data:', normalized_x)