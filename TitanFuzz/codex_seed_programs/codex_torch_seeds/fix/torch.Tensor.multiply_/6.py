'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply_\ntorch.Tensor.multiply_(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(5, 3)
print('Input tensor:', input_tensor)
torch.Tensor.multiply_(input_tensor, 2)
print('Output tensor:', input_tensor)
torch.Tensor.multiply_(input_tensor, 3, out=input_tensor)
print('Output tensor:', input_tensor)