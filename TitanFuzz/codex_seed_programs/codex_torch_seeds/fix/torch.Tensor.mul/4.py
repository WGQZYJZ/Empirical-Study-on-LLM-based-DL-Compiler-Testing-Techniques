'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(size=(3, 3))
print('Input Tensor: \n', input_tensor)
output_tensor = torch.Tensor.mul(input_tensor, 2)
print('Output Tensor: \n', output_tensor)