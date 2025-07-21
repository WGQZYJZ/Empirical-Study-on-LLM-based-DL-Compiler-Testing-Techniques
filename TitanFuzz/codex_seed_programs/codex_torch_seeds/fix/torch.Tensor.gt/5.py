'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gt\ntorch.Tensor.gt(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: \n', input_tensor)
output = input_tensor.gt(0)
print('Output Tensor: \n', output)