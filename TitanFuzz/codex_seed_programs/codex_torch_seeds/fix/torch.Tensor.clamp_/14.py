'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(_input_tensor, min=None, max=None)\n'
import torch
import torch
_input_tensor = torch.randn(10, 5)
torch.Tensor.clamp_(_input_tensor, min=0, max=1)
print(_input_tensor)