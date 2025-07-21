'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.angle\ntorch.angle(input, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
output_data = torch.angle(input_data)
print('Input data:', input_data)
print('Output data:', output_data)