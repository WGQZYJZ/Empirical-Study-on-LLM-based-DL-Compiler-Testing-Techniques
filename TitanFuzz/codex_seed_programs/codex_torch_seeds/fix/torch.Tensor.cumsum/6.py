'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(_input_tensor, dim, dtype=None)\n'
import torch
_input_tensor = torch.rand(1, 3, 4, 5)
print(_input_tensor)
_output_tensor = _input_tensor.cumsum(dim=1, dtype=torch.float)
print(_output_tensor)