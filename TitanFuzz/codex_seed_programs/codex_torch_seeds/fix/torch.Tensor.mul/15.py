'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul\ntorch.Tensor.mul(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor = \n{}'.format(input_tensor))
output_tensor = torch.Tensor.mul(input_tensor, 10)
print('output_tensor = \n{}'.format(output_tensor))