'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.max\ntorch.Tensor.max(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = _input_tensor.max(dim=1, keepdim=True)
print(_output_tensor)
'\nTask 4: Call the API torch.Tensor.max\ntorch.Tensor.max(_input_tensor, dim=None, keepdim=False)\n'
_output_tensor = _input_tensor.max(dim=1, keepdim=False)
print(_output_tensor)
'\nTask 5: Call the API torch.Tensor.max\ntorch.Tensor.max(_input_tensor, dim=None, keepdim=False)\n'