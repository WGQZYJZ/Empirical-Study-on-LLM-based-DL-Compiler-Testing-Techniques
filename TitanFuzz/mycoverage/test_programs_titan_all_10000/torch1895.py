import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(3, 4)
output_tensor = torch.argsort(input_tensor, dim=(- 1), descending=False)