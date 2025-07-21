'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flipud\ntorch.Tensor.flipud(_input_tensor)\n'
import torch
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
print('input_tensor:')
print(input_tensor)
output_tensor = torch.Tensor.flipud(input_tensor)
print('output_tensor:')
print(output_tensor)