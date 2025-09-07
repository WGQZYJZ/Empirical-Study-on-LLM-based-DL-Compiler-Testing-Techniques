import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.bool)
_output_tensor = torch.Tensor.bitwise_not(_input_tensor)