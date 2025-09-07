import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.index_fill(input_tensor, 0, torch.tensor([0, 0]), 0)