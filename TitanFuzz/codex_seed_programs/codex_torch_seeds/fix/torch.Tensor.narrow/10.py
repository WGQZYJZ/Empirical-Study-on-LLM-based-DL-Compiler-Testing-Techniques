'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.rand(10, 3, 3)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.narrow(input_tensor, 1, 0, 2)
print('Output tensor: \n', output_tensor)
output_tensor = torch.Tensor.narrow(input_tensor, 2, 0, 2)
print('Output tensor: \n', output_tensor)