'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(3, 4)
other = torch.ones(3, 4)
output_tensor = torch.Tensor.subtract_(input_tensor, other)
print(output_tensor)