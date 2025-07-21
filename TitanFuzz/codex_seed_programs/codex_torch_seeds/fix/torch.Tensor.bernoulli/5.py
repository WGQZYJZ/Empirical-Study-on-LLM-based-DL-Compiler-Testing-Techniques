'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli\ntorch.Tensor.bernoulli(_input_tensor, *, generator=None)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
output_tensor = input_tensor.bernoulli()
print(output_tensor)