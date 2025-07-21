'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm_\ntorch.Tensor.renorm_(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
print(torch.Tensor.renorm_(input_tensor, 1, 0, 1))