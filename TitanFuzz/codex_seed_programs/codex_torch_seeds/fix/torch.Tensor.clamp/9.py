'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
output_tensor = input_tensor.clamp(min=(- 0.5), max=0.5)
print(output_tensor)