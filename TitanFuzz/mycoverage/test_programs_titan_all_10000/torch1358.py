import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 4, 5)
_output_tensor = torch.Tensor.dense_dim(_input_tensor)