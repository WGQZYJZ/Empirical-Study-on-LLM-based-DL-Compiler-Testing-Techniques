'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil\ntorch.Tensor.ceil(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor:\n', input_tensor)
output_tensor = torch.Tensor.ceil(input_tensor)
print('Output Tensor:\n', output_tensor)