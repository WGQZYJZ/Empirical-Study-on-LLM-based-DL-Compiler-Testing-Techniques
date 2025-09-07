import torch
from torch import nn
from torch.autograd import Variable

_output_tensor = torch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)