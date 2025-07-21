'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm_\ntorch.Tensor.renorm_(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.randn(1, 4)
output_tensor = input_tensor.renorm_(2, 1, 1)
print('Input tensor: \n', input_tensor)
print('Output tensor: \n', output_tensor)