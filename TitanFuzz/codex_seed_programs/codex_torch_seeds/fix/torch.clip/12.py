'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clip\ntorch.clip(input, min=None, max=None, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('input_data:', input_data)
output_data = torch.clip(input_data, (- 0.5), 0.5)
print('output_data:', output_data)