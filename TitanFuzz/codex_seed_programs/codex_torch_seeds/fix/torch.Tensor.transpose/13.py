'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(3, 4, 5)
output_tensor = torch.Tensor.transpose(input_tensor, 0, 1)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
input_tensor = torch.randn(3, 4, 5)
output_tensor = torch.Tensor.flip(input_tensor, [1])
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)