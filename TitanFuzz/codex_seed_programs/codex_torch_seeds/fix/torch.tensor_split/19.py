'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input_data = torch.arange(start=0, end=24, dtype=torch.float32).reshape(2, 3, 4)
print('input_data = ', input_data)
output_data = torch.tensor_split(input_data, [1, 2, 1], dim=0)
print('output_data = ', output_data)