'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm_\ntorch.Tensor.renorm_(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.rand(10, 2)
torch.Tensor.renorm_(input_tensor, 1, 0, 10)
print(input_tensor)