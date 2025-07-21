'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('Input tensor:')
print(input_tensor)
print('Output tensor:')
print(input_tensor.ravel())