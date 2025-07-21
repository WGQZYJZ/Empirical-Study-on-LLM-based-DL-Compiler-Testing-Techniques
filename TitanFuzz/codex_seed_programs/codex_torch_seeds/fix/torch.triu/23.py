'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.triu\ntorch.triu(input, diagonal=0, *, out=None)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data is: ', input_data)
output_data = torch.triu(input_data)
print('Output data is: ', output_data)