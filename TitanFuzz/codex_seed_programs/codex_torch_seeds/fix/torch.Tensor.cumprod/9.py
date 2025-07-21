'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4)
_input_tensor = torch.randn(2, 3, 4)
_dim = 1
_dtype = None
_output = _input_tensor.cumprod(_dim, _dtype)
print('Output = ', _output)