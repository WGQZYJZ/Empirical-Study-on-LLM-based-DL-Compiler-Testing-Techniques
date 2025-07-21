import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 4, 4)
output_tensor = torch.Tensor.new_full(input_tensor, 3, dtype=torch.float32)