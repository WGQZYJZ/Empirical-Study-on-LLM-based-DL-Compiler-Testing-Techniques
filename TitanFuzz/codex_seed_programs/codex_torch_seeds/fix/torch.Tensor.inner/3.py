'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inner\ntorch.Tensor.inner(_input_tensor, other)\n'
import torch
a = torch.randn(4, 3)
b = torch.randn(3, 4)
torch.Tensor.inner(a, b)