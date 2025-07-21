import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 1, 4, 4)
output_tensor = torch.broadcast_tensors(input_tensor, input_tensor)