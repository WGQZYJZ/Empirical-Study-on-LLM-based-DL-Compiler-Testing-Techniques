import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.int8)
other = torch.randint(0, 2, (3, 3), dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_or_(input_tensor, other)