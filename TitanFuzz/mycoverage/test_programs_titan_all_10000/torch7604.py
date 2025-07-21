import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.bool)
other = torch.randint(0, 2, (2, 3), dtype=torch.bool)
torch.Tensor.logical_or_(_input_tensor, other)
_input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.bool)
other = torch.randint(0, 2, (2, 3), dtype=torch.bool)
torch.Tensor.logical_or(_input_tensor, other)