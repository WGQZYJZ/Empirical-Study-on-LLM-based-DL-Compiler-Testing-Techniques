import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]])
shape = (2, 2, 2)
output_tensor = torch.broadcast_to(input_tensor, shape)