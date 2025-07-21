'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.add\ntorch.add(input, other, *, alpha=1, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print('input_data:')
print(input_data)
other_data = torch.randn(5, 3)
print('other_data:')
print(other_data)
output_data = torch.add(input_data, other_data)
print('output_data:')
print(output_data)