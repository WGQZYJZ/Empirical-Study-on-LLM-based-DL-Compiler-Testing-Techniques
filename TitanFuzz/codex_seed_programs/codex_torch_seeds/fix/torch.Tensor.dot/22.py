'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dot\ntorch.Tensor.dot(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(1, 3)
other = torch.rand(3, 1)
_output_tensor = torch.Tensor.dot(_input_tensor, other)
print(_output_tensor)