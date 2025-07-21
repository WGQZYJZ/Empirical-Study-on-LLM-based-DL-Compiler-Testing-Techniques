'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh\ntorch.Tensor.arccosh(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3, 3)
output_tensor = torch.Tensor.arccosh(input_tensor)
print('Input Tensor : ', input_tensor)
print('Output Tensor : ', output_tensor)