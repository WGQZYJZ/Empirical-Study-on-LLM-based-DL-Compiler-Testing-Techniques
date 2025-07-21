'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp\ntorch.Tensor.ldexp(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.Tensor([[(- 1), 2, 3], [4, 5, 6]])
output_tensor = input_tensor.ldexp(2)
print('Input: {}'.format(input_tensor))
print('Output: {}'.format(output_tensor))