'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.rand(2, 3, 4)
output_data = torch.rand(2, 3, 4)
print('Input data: ', input_data)
print('Output data: ', output_data)
print('Data type of input data: ', input_data.dtype)
print('Data type of output data: ', output_data.dtype)
print('Size of input data: ', input_data.size())
print('Size of output data: ', output_data.size())
print('Layout of input data: ', input_data.layout)
print('Layout of output data: ', output_data.layout)