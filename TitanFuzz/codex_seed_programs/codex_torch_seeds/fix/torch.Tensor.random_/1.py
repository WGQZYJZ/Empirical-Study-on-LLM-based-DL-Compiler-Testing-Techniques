'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.random_\ntorch.Tensor.random_(_input_tensor, from=0, to=None, *, generator=None)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
print(input_tensor)
random_tensor = torch.Tensor.random_(input_tensor, from_=1, to=10)
print(random_tensor)