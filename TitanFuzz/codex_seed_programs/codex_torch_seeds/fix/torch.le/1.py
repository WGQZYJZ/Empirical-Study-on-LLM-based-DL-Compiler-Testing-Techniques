'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
import torch
'\nTask 1: Generate input data\n'
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input Data:\n', input_data)
'\nTask 2: Call the API torch.le\ntorch.le(input, other, *, out=None)\n'
output_data = torch.le(input_data, torch.tensor([[1, 2, 3], [4, 5, 6]]))
print('Output Data:\n', output_data)