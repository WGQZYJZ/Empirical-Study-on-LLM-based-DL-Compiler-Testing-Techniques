'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dist\ntorch.Tensor.dist(_input_tensor, other, p=2)\n'
import torch
input_tensor = torch.randn(1, 3)
print(input_tensor)
output_tensor = torch.Tensor.dist(input_tensor, input_tensor, p=2)
print(output_tensor)