'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gt\ntorch.Tensor.gt(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input Tensor: \n', input_tensor)
output_tensor = input_tensor.gt(0.5)
print('Output Tensor: \n', output_tensor)