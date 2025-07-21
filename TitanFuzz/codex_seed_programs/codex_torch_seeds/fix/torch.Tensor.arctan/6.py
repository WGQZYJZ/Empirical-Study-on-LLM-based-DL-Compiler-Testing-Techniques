'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan\ntorch.Tensor.arctan(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.arctan(input_tensor)
print('input_tensor = \n', input_tensor)
print('output_tensor = \n', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.arctan(input_tensor)
print('input_tensor = \n', input_tensor)
print('output_tensor = \n', output_tensor)