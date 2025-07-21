'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli_\ntorch.Tensor.bernoulli_(_input_tensor, p=0.5, *, generator=None)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: \n', _input_tensor)
_output_tensor = torch.Tensor.bernoulli_(_input_tensor, p=0.5, generator=None)
print('Output tensor: \n', _output_tensor)