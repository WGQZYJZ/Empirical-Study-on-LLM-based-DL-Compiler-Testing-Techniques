'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
_input_tensor = torch.randn(8, 4)
_split_tensor = _input_tensor.split(split_size=2, dim=0)
print('The input tensor is: ', _input_tensor)
print('The split tensor is: ', _split_tensor)