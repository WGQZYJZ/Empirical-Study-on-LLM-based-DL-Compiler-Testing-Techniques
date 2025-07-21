'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
_input_tensor = torch.randint(10, (3, 3))
print('Input tensor: \n', _input_tensor)
mask = torch.ByteTensor([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
print('Mask: \n', mask)
source = torch.randint(10, (3,))
print('Source: \n', source)
torch.Tensor.masked_scatter_(_input_tensor, mask, source)
print('Output tensor: \n', _input_tensor)