import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(10)
output_tensor = torch.special.erfcx(input_tensor)