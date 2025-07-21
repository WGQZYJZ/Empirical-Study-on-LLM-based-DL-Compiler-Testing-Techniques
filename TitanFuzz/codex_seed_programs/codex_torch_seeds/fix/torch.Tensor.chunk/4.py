'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
import torch
input_tensor = torch.randn(8, 3)
output_tensor = input_tensor.chunk(3, dim=0)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min, max, out=None)\n'
import torch
import torch
input_tensor = torch.randn(4, 4)
output_tensor = input_tensor.clamp(min=0.2, max=0.8)
print(output_tensor)