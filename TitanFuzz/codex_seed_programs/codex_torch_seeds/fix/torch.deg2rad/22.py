'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.deg2rad\ntorch.deg2rad(input, *, out=None)\n'
import torch
input_data = torch.tensor([0.0, 30.0, 45.0, 60.0, 90.0])
print('Input in degrees')
print(input_data)
print('Output in radians')
print(torch.deg2rad(input_data))