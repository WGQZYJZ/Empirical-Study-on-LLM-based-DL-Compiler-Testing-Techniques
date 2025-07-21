import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor(3, 3)
torch.Tensor.resize_as_(input_tensor, output_tensor)
output_tensor = torch.Tensor(3, 3)
torch.Tensor.resize_(input_tensor, (3, 3))