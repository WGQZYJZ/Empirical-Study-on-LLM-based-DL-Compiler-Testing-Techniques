'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli\ntorch.Tensor.bernoulli(_input_tensor, *, generator=None)\n'
import torch
import torch
input_tensor = torch.Tensor([0, 1, 0, 1, 1])
bernoulli_tensor = torch.Tensor.bernoulli(input_tensor)
print(bernoulli_tensor)