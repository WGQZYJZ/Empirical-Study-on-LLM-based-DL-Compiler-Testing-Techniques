'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isposinf\ntorch.Tensor.isposinf(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor:')
print(input_tensor)
print('\nOutput Tensor:')
print(input_tensor.isposinf())