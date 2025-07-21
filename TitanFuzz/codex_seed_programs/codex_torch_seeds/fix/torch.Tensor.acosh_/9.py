'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acosh_\ntorch.Tensor.acosh_(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('input_tensor: ', input_tensor)
output_tensor = torch.acosh(input_tensor)
print('output_tensor: ', output_tensor)
input_tensor.acosh_()
print('input_tensor: ', input_tensor)