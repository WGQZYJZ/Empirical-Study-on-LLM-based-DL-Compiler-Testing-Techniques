'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diag_embed\ntorch.diag_embed(input, offset=0, dim1=-2, dim2=-1)\n'
import torch
input_data = torch.rand(2, 3, 4)
print('Input data: \n', input_data)
output_data = torch.diag_embed(input_data, offset=0, dim1=(- 2), dim2=(- 1))
print('Output data: \n', output_data)