'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = input_tensor.add(10)
print(output_tensor)