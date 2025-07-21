'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
print('Input tensor: ', _input_tensor)
_squeeze_tensor = torch.Tensor.squeeze(_input_tensor, dim=None)
print('Squeeze tensor: ', _squeeze_tensor)