'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
input_data = torch.randn(5, 3)
print('Input data:')
print(input_data)
print('Output:')
print(torch.count_nonzero(input_data, dim=0))