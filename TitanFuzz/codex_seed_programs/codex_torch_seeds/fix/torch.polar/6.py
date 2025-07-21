'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polar\ntorch.polar(abs, angle, *, out=None)\n'
import torch
abs_data = torch.randn(2, 3, 4)
angle_data = torch.randn(2, 3, 4)
output = torch.polar(abs_data, angle_data)
print('output =', output)