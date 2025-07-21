'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.scatter\ntorch.scatter(input, dim, index, src)\n'
import torch
input_data = torch.randn(3, 4)
print('input_data: {}'.format(input_data))
output_data = torch.scatter(input_data, 1, torch.tensor([[2], [0], [1]]), 0.5)
print('output_data: {}'.format(output_data))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.scatter_add\ntorch.scatter_add(input, dim, index, src)\n'
import torch
input_data = torch.randn(3, 4)
print('input_data: {}'.format(input_data))