'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erf\ntorch.special.erf(input, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
output_data = torch.special.erf(input_data)
print('Output data: ', output_data)
'\ntorch.special.erfinv(input, *, out=None)\n'
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
output_data = torch.special.erfinv(input_data)
print('Output data: ', output_data)
'\ntorch.special.expit(input, *, out=None)\n'
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
output_data = torch.special.expit(input_data)
print('Output data: ', output_data)