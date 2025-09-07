import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.Tensor([(- 1), 0, 1])
output_data = torch.sgn(input_data)