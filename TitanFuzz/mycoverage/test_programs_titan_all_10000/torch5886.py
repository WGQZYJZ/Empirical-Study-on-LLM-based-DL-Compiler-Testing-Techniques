import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 1], [1, 1], [1, 1], [0, 0]])
other_tensor = torch.tensor([[0, 1], [1, 1], [1, 1], [0, 0]])
output_tensor = torch.Tensor.not_equal(input_tensor, other_tensor)