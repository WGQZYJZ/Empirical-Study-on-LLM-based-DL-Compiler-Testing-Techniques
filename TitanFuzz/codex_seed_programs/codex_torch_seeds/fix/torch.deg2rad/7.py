'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.deg2rad\ntorch.deg2rad(input, *, out=None)\n'
import torch
input = torch.tensor([0, 30, 45, 60, 90])
print('Input in degrees:', input)
output = torch.deg2rad(input)
print('Output in radians:', output)