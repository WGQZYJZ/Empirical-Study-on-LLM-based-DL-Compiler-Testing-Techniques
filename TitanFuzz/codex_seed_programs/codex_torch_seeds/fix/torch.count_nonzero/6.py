'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input_data = torch.tensor([[0, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
print('Input data: ', input_data)
output_data = torch.count_nonzero(input_data)
print('Output data: ', output_data)