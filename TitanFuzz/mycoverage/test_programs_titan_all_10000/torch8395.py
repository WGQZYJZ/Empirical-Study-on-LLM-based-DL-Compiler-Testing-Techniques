import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 10, (2, 3, 2))
_output_tensor = torch.Tensor.ravel(_input_tensor)