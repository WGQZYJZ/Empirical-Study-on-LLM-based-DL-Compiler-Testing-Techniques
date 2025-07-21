'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
import torch
input_tensor = torch.rand(2, 2)
print('input_tensor:', input_tensor)
n = 2
output_tensor = input_tensor.matrix_power(n)
print('output_tensor:', output_tensor)