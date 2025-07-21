'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagflat\ntorch.Tensor.diagflat(_input_tensor, offset=0)\n'
import torch
input_tensor = torch.randn(5, 3)
print('Input Tensor: ', input_tensor)
output_tensor = torch.Tensor.diagflat(input_tensor, offset=1)
print('Output Tensor: ', output_tensor)