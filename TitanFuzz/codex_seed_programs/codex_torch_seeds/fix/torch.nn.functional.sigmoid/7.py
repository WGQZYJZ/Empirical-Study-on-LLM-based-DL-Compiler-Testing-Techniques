'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.sigmoid\ntorch.nn.functional.sigmoid(input)\n'
import torch
input_data = torch.tensor([1.0, 2.0, 3.0])
output_data = torch.nn.functional.sigmoid(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)