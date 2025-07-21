import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=10, size=(2, 3))
output_tensor = torch.Tensor.diagflat(input_tensor, offset=0)
output_tensor = torch.diagflat(input_tensor, offset=0)