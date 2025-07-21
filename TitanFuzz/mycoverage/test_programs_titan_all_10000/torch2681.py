import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(10, (2, 3), dtype=torch.int32)
output_tensor = torch.Tensor.int_repr(input_tensor)