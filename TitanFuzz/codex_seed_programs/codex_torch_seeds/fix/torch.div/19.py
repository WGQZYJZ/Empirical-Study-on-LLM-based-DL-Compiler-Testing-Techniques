'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
input_data = torch.randn(2, 2)
print('input_data:', input_data)
output_data = torch.div(input_data, input_data)
print('output_data:', output_data)