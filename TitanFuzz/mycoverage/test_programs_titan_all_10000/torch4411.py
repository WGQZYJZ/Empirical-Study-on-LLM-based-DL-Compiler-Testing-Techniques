import torch
from torch import nn
from torch.autograd import Variable
tensor_input = torch.rand(2, 3)
arccos_result = torch.Tensor.arccos(tensor_input)