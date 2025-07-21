'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inverse\ntorch.Tensor.inverse(_input_tensor)\n'
import torch
_input_tensor = torch.rand(4, 4)
_inverse_tensor = torch.Tensor.inverse(_input_tensor)
print(_inverse_tensor)