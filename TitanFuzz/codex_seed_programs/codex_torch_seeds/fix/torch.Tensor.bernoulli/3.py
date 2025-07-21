'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli\ntorch.Tensor.bernoulli(_input_tensor, *, generator=None)\n'
import torch
input_tensor = torch.randn(1, 2, 3)
print(input_tensor)
output_tensor = torch.Tensor.bernoulli(input_tensor)
print(output_tensor)