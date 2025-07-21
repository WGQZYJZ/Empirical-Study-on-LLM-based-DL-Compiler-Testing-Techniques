'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randn(4, 4)
mask = torch.ByteTensor([[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]])
value = (- 1)
input_tensor.masked_fill_(mask, value)
print('Input Tensor: \n', input_tensor)