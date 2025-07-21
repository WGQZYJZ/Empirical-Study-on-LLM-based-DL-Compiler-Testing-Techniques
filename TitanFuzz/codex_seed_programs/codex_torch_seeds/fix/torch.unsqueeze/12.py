'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print('Input data: {}'.format(input_data))
output_data = torch.unsqueeze(input_data, dim=1)
print('Output data: {}'.format(output_data))