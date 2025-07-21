import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([3.1, (- 3.1), 4.8, (- 4.8)])
output = torch.ceil(input_data)