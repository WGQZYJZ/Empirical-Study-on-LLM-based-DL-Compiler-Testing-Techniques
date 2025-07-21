import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 10, (4, 4))
_output_tensor = torch.Tensor.vsplit(_input_tensor, 2)