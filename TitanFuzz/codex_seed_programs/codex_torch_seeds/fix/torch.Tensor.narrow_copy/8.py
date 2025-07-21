'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randn(10, 3)
print('Input tensor:')
print(input_tensor)
import torch
input_tensor = torch.randn(10, 3)
print('Input tensor:')
print(input_tensor)
output_tensor = input_tensor.narrow_copy(dim=1, start=0, length=2)
print('Output tensor:')
print(output_tensor)