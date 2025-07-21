import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 1, 0], [1, 0, 1]])
other_tensor = torch.tensor([[1, 0, 1], [0, 1, 0]])
output_tensor = torch.Tensor.bitwise_and_(input_tensor, other_tensor)