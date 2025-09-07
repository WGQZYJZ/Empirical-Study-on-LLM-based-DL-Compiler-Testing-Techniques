import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(low=0, high=10, size=(2, 3))
_median = torch.Tensor.median(_input_tensor)