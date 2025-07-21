import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 3)
arctan_result = torch.Tensor.arctan(input_tensor)