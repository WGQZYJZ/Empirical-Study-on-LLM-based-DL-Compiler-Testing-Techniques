'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input_data = torch.randn(2, 3, 5)
print('Input data: \n', input_data)
output_data = torch.permute(input_data, (2, 0, 1))
print('Output data: \n', output_data)