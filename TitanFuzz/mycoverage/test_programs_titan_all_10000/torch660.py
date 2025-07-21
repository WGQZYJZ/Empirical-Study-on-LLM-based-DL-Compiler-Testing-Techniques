import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
data = torch.randn(2, 3)
output_tensor = torch.Tensor.new_tensor(input_tensor, data)