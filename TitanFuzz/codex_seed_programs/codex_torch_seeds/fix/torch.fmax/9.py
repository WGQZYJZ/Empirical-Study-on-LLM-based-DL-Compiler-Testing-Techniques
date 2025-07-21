'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
other_data = torch.randn(3, 4)
output_data = torch.fmax(input_data, other_data)
print('input_data:', input_data)
print('other_data:', other_data)
print('output_data:', output_data)