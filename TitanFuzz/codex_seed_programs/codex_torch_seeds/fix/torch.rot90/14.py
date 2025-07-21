'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input_data = torch.rand(3, 4)
print('Input data: ', input_data)
rotated_data = torch.rot90(input_data, 2, dims=(0, 1))
print('Rotated data: ', rotated_data)