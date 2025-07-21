'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.angle\ntorch.angle(input, *, out=None)\n'
import torch
input_data = torch.rand(2, 2)
print('Input data is: ', input_data)
angle = torch.angle(input_data)
print('Angle is: ', angle)