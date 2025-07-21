'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.le_\ntorch.Tensor.le_(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
output_tensor = torch.Tensor.le_(input_tensor, other)
print('Input Tensor : \n', input_tensor)
print('Other Tensor : \n', other)
print('Output Tensor : \n', output_tensor)