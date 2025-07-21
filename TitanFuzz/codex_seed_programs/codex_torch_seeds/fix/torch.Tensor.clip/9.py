'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip\ntorch.Tensor.clip(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
output_tensor = torch.Tensor.clip(input_tensor, min=(- 0.5), max=0.5)
print(output_tensor)