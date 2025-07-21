import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = torch.Tensor.q_scale(input_tensor)