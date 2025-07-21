import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([(- float('inf')), (- 1), 0, 1, float('inf')])
output_tensor = torch.Tensor.isneginf(input_tensor)