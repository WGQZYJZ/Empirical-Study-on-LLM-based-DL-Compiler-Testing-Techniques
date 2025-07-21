'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rot90\ntorch.rot90(input, k, dims)\n'
import torch
input_data = torch.arange(1, 10).view(3, 3)
print('Input data:')
print(input_data)
output_data = torch.rot90(input_data, 1, dims=(1, 0))
print('Output data:')
print(output_data)