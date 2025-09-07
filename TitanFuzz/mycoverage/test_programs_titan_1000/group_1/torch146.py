import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(low=0, high=2, size=(2, 3), dtype=torch.int32)
other = torch.randint(low=0, high=2, size=(2, 3), dtype=torch.int32)
_output_tensor = torch.Tensor.logical_or(_input_tensor, other)