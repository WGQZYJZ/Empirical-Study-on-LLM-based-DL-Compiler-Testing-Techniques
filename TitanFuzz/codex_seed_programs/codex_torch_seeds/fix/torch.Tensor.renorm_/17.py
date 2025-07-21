'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm_\ntorch.Tensor.renorm_(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.randn(5, 3)
torch.Tensor.renorm_(input_tensor, 1, 0, 10)
print(input_tensor)