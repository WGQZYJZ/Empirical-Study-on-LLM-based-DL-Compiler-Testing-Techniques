'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.smm\ntorch.Tensor.smm(_input_tensor, mat)\n'
import torch
input_tensor = torch.randn(2, 3)
mat = torch.randn(3, 3)
output_tensor = torch.Tensor.smm(input_tensor, mat)
print('input_tensor:\n', input_tensor)
print('mat:\n', mat)
print('output_tensor:\n', output_tensor)