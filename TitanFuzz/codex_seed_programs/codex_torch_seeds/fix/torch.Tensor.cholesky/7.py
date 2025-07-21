'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky\ntorch.Tensor.cholesky(_input_tensor, upper=False)\n'
import torch
input_tensor = torch.rand(2, 2)
print('Input tensor: \n', input_tensor)
output_tensor = input_tensor.cholesky(upper=False)
print('Output tensor: \n', output_tensor)