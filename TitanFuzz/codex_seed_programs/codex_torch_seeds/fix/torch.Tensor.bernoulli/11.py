'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli\ntorch.Tensor.bernoulli(_input_tensor, *, generator=None)\n'
import torch
input_tensor = torch.rand(4, 4)
print(input_tensor)
print(torch.Tensor.bernoulli(input_tensor))
print(torch.Tensor.bernoulli(input_tensor, generator=None))
print(torch.Tensor.bernoulli(input_tensor, generator=torch.Generator()))