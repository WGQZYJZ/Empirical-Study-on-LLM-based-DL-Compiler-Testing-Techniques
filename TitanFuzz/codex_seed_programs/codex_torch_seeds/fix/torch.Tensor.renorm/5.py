'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm\ntorch.Tensor.renorm(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.randn(4, 4)
print('input_tensor: \n{}'.format(input_tensor))
output_tensor = torch.Tensor.renorm(input_tensor, p=2, dim=0, maxnorm=1)
print('output_tensor: \n{}'.format(output_tensor))