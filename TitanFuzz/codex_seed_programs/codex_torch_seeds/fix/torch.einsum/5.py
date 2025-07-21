'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
import torch
input_data = torch.rand(2, 3, 4)
output_data = torch.einsum('ijk,ijl->ikl', input_data, input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)
print('output_data.shape: ', output_data.shape)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
import torch
input_data = torch.rand(2, 3, 4)
output_data = torch.einsum('ijk,ijl->ikl', input_data, input_data)