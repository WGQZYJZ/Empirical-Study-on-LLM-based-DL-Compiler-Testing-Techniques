'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip_\ntorch.Tensor.clip_(_input_tensor, min=None, max=None)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 10, 10)
output_tensor = torch.Tensor.clip_(input_tensor, min=(- 1), max=1)
print(input_tensor)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp_\ntorch.Tensor.clamp_(input_tensor, min=None, max=None)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 10, 10)
output_tensor = torch.Tensor.clamp_(input_tensor, min=(- 1), max=1)