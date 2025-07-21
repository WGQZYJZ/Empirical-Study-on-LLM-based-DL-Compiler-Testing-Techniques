'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randn(5, 5)
print('Input tensor:')
print(input_tensor)
dimension = 0
start = 2
length = 2
output_tensor = torch.Tensor.narrow_copy(input_tensor, dimension, start, length)
print('Output tensor:')
print(output_tensor)