'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor: \n', input_tensor)
mask = torch.ByteTensor([[0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]])
print('Mask: \n', mask)
value = (- 1)
output_tensor = input_tensor.masked_fill_(mask, value)
print('Output Tensor: \n', output_tensor)