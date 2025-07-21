'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ge\ntorch.Tensor.ge(_input_tensor, other)\n'
import torch
input_tensor = torch.zeros(2, 3)
print('Input tensor:\n{}'.format(input_tensor))
other = torch.ones(2, 3)
output_tensor = input_tensor.ge(other)
print('Output tensor:\n{}'.format(output_tensor))