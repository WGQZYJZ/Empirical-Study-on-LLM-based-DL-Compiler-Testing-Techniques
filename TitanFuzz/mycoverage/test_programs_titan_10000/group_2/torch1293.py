import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([[0, 1, 0], [1, 1, 0], [1, 1, 1]], dtype=torch.bool)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)