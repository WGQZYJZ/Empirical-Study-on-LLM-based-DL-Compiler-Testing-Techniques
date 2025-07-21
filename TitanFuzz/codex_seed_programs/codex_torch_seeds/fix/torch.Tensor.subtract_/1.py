'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(10, requires_grad=True)
other = torch.randn(10)
output_tensor = input_tensor.subtract_(other)
print(output_tensor)