'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cosh\ntorch.Tensor.cosh(_input_tensor)\n'
import torch
import torch
input_tensor = torch.arange((- 5), 5, 0.1)
output_tensor = torch.Tensor.cosh(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)