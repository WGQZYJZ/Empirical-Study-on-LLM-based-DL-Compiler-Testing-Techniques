'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm\ntorch.Tensor.renorm(_input_tensor, p, dim, maxnorm)\n'
import torch
from torch.autograd import Variable
input_tensor = torch.randn(5, 3)
print('Input tensor:')
print(input_tensor)
output_tensor = torch.Tensor.renorm(input_tensor, 2, 0, 5)
print('Output tensor:')
print(output_tensor)