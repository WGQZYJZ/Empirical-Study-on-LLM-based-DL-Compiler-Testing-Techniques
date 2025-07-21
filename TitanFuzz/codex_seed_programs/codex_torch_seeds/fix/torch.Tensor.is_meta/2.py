'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_meta\ntorch.Tensor.is_meta(_input_tensor, )\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
input_tensor = torch.randn(5, 5)
output_tensor = torch.Tensor.is_meta(input_tensor)
print(output_tensor)