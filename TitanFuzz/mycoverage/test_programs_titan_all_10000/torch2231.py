import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(size=(1, 3, 224, 224))
_output_tensor = torch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)