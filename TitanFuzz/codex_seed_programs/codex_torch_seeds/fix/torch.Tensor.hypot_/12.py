'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot_\ntorch.Tensor.hypot_(_input_tensor, other)\n'
import torch
input_data = torch.randn(2, 3)
other = torch.randn(2, 3)
output = torch.Tensor.hypot_(input_data, other)
print('Input data: \n{}'.format(input_data))
print('Other: \n{}'.format(other))
print('Output: \n{}'.format(output))