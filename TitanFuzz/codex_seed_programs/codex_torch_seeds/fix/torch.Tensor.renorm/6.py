'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm\ntorch.Tensor.renorm(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.ones(2, 3)
print(input_tensor)
output_tensor = input_tensor.renorm(p=1, dim=0, maxnorm=2)
print(output_tensor)