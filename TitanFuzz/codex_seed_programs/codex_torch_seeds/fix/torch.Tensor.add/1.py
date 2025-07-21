'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
output_tensor = input_tensor.add(other)
print(output_tensor)
output_tensor = input_tensor.add_(other)
print(output_tensor)
output_tensor = input_tensor.add(other, alpha=2)
print(output_tensor)
output_tensor = input_tensor.add_(other, alpha=2)
print(output_tensor)
output_tensor = input_tensor.add(other, alpha=2.5)