import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(1, 13)
output_tensor = torch.Tensor.unfold(input_tensor, 0, 2, 2)