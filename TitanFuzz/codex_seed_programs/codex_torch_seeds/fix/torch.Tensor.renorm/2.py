'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm\ntorch.Tensor.renorm(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.rand(1, 3, 2, 2)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.renorm(p=2, dim=1, maxnorm=1)
print('output_tensor: ', output_tensor)