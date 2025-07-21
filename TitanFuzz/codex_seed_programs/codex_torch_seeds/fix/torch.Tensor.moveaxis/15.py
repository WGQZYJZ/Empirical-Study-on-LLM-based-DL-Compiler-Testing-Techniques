'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.rand((3, 4, 5))
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.moveaxis(input_tensor, 2, 0)
print('Output tensor: \n', output_tensor)