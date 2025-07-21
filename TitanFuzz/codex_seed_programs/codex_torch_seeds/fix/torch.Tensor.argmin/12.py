'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = _input_tensor.argmin(dim=2, keepdim=True)
print(_output_tensor)