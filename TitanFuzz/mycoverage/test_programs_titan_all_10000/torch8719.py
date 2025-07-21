import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1), 2])
output_data = torch.le(input_data, 0)