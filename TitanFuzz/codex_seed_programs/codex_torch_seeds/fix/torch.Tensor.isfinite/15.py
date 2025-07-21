'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isfinite\ntorch.Tensor.isfinite(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output = torch.Tensor.isfinite(_input_tensor)
print(_output)