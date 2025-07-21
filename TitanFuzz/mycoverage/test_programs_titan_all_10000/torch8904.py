import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([True, False, True, False], dtype=torch.bool)
output_tensor = torch.bitwise_not(input_tensor)