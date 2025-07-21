'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
input_tensor = torch.arange(1, 11, dtype=torch.float32).reshape(2, 5)
print('Input tensor: \n', input_tensor)
output_tensor = input_tensor.pow(2)
print('Output tensor: \n', output_tensor)
input_tensor.pow_(3)
print('Input tensor: \n', input_tensor)
output_tensor = torch.pow(input_tensor, 3)
print('Output tensor: \n', output_tensor)