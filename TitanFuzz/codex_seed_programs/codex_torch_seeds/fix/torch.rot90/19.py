'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input_data = torch.arange(1, 37).view(2, 3, 6)
print('Input data: ', input_data)
output_data = torch.rot90(input_data, 1, dims=(0, 2))
print('Output data: ', output_data)