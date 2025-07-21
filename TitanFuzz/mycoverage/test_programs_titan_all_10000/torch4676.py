import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.bool)
other = torch.randint(0, 2, (3, 3), dtype=torch.bool)
result = torch.Tensor.bitwise_or_(_input_tensor, other)