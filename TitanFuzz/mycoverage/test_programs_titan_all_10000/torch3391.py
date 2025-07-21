import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(2, 3, 4)
torch.Tensor.is_floating_point(input_tensor)
input_tensor = torch.randn(2, 3, 4)
torch.Tensor.is_complex(input_tensor)