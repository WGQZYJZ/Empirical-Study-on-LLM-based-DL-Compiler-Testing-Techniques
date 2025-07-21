'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([2.0, 3.0, 4.0])
output_data = torch.square(input_data)
print('input_data:', input_data)
print('output_data:', output_data)
output_data = torch.sqrt(input_data)
print('input_data:', input_data)
print('output_data:', output_data)
output_data = torch.pow(input_data, 2)
print('input_data:', input_data)
print('output_data:', output_data)
output_data = torch.exp(input_data)
print('input_data:', input_data)
print('output_data:', output_data)