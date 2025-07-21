'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.deg2rad\ntorch.deg2rad(input, *, out=None)\n'
import torch
input = torch.tensor([(- 180.0), (- 90.0), 0.0, 90.0, 180.0])
output = torch.deg2rad(input)
print('output = ', output)