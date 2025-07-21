'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor:')
print(input_tensor)
output_tensor = input_tensor.ravel()
print('Output tensor:')
print(output_tensor)