import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
output_tensor = torch.Tensor.logical_not_(input_tensor)