'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cov\ntorch.Tensor.cov(_input_tensor, *, correction=1, fweights=None, aweights=None)\n'
import torch
input_tensor = torch.rand(100, 3)
print(input_tensor.cov())