'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli\ntorch.Tensor.bernoulli(_input_tensor, *, generator=None)\n'
import torch
import torch
input_data = torch.randn(1, 3)
print(input_data)
torch.Tensor.bernoulli(input_data)
print(input_data)
torch.Tensor.bernoulli(input_data, 0.5)
print(input_data)
torch.Tensor.bernoulli(input_data, torch.empty(1, 3).uniform_(0.3, 0.7))
print(input_data)
torch.Tensor.bernoulli(input_data, torch.empty(1, 3).uniform_(0.3, 0.7), generator=torch.Generator())
print(input_data)