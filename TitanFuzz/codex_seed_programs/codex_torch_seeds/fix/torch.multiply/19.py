'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.multiply\ntorch.multiply(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
output_data = torch.multiply(input_data, 2)
print('input_data: ', input_data)
print('output_data: ', output_data)