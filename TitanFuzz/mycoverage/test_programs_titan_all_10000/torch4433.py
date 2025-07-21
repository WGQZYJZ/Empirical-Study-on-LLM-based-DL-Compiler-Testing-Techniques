import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, (- 1), 3, (- 3)], [4, (- 4), 6, (- 6)]])
other = torch.tensor([[1, 1, 1, 1], [1, 1, 1, 1]])
output_tensor = torch.Tensor.copysign_(input_tensor, other)