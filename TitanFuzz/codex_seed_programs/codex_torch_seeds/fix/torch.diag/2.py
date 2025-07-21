'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag\ntorch.diag(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(4, 5)
print('Input data: ', input_data)
output_data = torch.diag(input_data)
print('Output data: ', output_data)