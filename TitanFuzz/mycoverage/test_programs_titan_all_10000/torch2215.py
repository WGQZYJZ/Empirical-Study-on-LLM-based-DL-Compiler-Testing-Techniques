import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.new_full(input_tensor, 3, fill_value=0.5)
output_tensor = torch.Tensor.new_full(input_tensor, 3, fill_value=0.5, dtype=torch.int32)