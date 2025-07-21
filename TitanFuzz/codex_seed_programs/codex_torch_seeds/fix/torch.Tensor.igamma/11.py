'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma\ntorch.Tensor.igamma(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
_output_tensor = torch.Tensor.igamma(_input_tensor, other)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)