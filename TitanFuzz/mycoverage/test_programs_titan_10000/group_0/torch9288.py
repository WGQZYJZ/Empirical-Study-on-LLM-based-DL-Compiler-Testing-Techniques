import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.tensor([(- 1), (- 2), 3])
output = torch.abs(input_data)