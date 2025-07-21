'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm_\ntorch.Tensor.renorm_(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.randn(4, 3)
print(input_tensor)
output_tensor = torch.Tensor.renorm_(input_tensor, p=2, dim=1, maxnorm=1)
print(output_tensor)