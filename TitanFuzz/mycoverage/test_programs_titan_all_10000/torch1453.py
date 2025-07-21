import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_clone_tensor = torch.Tensor.clone(_input_tensor)