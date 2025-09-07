import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1.0, 2.0], [1.0, 2.0]])
output_tensor = torch.Tensor.angle(input_tensor)