'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
x = torch.randn(1, 3, dtype=torch.float)
print('Input data:', x)
y = torch.special.erfinv(x)
print('Output data:', y)