import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.tensor([(- 2), (- 1), 0, 1, 2])
output = torch.neg(input_data)