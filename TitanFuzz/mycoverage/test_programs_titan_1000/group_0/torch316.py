import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 17, dtype=torch.float).view(4, 4)
output_data = torch.triu_indices(row=4, col=4, offset=0)