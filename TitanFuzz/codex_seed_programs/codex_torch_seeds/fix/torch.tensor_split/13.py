'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input_data = torch.arange(1, 13)
print('Input data: ', input_data)
split_data = torch.tensor_split(input_data, 4, dim=0)
print('Split data: ', split_data)