'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape_as\ntorch.Tensor.reshape_as(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: ', input_tensor)
other_tensor = torch.randn(3, 2)
print('other_tensor: ', other_tensor)
output_tensor = input_tensor.reshape_as(other_tensor)
print('output_tensor: ', output_tensor)