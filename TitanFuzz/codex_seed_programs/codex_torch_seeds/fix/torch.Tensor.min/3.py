'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.min\ntorch.Tensor.min(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = _input_tensor.min(dim=1, keepdim=True)
print(_output_tensor)