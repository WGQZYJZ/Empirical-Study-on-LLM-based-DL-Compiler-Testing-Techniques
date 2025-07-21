'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sub\ntorch.sub(input, other, *, alpha=1, out=None)\n'
import torch
input_data = torch.rand(3, 3)
other_data = torch.rand(3, 3)
output_data = torch.sub(input_data, other_data)
print('input_data:', input_data)
print('other_data:', other_data)
print('output_data:', output_data)