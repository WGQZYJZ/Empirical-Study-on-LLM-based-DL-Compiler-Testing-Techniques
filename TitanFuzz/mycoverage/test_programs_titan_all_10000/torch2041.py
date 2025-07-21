import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([(- 1), 0, 1], dtype=torch.float32)
output = torch.Tensor.heaviside(input_tensor, 0.5)