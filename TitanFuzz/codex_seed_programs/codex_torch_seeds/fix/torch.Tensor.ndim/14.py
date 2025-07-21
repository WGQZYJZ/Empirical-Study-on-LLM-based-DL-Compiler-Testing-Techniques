'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndim\ntorch.Tensor.ndim(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 4)
_output = torch.Tensor.ndim(_input_tensor)
print(_output)