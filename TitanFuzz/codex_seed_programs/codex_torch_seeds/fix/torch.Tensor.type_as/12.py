'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3, 3)
from torch import Tensor
input_tensor = Tensor(1, 3, 3, 3).normal_()
output_tensor = input_tensor.type_as(input_tensor)
print('Input Tensor: {}'.format(input_tensor))
print('Output Tensor: {}'.format(output_tensor))