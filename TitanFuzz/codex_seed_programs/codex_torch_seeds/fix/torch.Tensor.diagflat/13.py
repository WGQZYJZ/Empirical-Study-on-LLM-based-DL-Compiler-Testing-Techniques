'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diagflat\ntorch.Tensor.diagflat(_input_tensor, offset=0)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor: ', input_tensor)
print('Output tensor: ', torch.Tensor.diagflat(input_tensor))
print('Output tensor: ', torch.Tensor.diagflat(input_tensor, offset=1))
print('Output tensor: ', torch.Tensor.diagflat(input_tensor, offset=(- 1)))