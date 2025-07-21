'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sqrt\ntorch.Tensor.sqrt(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
_sqrt_output = torch.Tensor.sqrt(_input_tensor)
print(_sqrt_output)