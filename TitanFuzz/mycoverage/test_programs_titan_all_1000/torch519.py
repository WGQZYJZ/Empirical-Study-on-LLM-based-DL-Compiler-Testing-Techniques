import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1, (- 1), 0.5, (- 0.5)])
output = torch.acos(input_data)