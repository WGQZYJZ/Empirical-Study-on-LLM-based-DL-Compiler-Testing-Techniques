'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide_\ntorch.Tensor.floor_divide_(_input_tensor, value)\n'
import torch
import torch
input_tensor = torch.rand(5, 5)
print('Input Tensor: \n', input_tensor)
output_tensor = torch.Tensor.floor_divide_(input_tensor, 2)
print('Output Tensor: \n', output_tensor)