import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn((1, 3, 224, 224))
_output_tensor = torch.Tensor.log10(_input_tensor)