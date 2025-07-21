'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.randn(3, 4))
print('Input tensor:', input_tensor)
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=None, keepdim=False)
print('Output tensor:', output_tensor)