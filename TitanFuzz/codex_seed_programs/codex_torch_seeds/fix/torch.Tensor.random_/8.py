'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.random_\ntorch.Tensor.random_(_input_tensor, from=0, to=None, *, generator=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
torch.Tensor.random_(input_data, from_=0, to=None, generator=None)
print(input_data)