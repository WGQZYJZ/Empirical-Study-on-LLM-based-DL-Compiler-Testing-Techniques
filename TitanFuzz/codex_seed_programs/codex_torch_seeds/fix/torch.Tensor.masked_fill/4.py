'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: {}'.format(input_tensor))
mask = torch.ByteTensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
print('Mask: {}'.format(mask))
value = torch.tensor(1.0)
print('Value: {}'.format(value))
output_tensor = input_tensor.masked_fill(mask, value)
print('Output Tensor: {}'.format(output_tensor))