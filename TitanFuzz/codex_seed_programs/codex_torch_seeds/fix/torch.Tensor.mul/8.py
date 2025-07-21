'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = torch.Tensor.mul(input_tensor, 2)
print('input_tensor: {}'.format(input_tensor))
print('output_tensor: {}'.format(output_tensor))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = torch.Tensor.div(input_tensor, 2)
print('input_tensor: {}'.format(input_tensor))