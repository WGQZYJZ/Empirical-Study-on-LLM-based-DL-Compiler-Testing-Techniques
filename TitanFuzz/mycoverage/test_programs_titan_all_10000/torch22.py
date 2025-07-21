import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 0.5), 0.5])
output_data = torch.erfinv(input_data)