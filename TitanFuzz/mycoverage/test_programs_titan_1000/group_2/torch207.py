import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=10, size=(2, 3, 4))
output_tensor = torch.Tensor.resize_(input_tensor, (2, 3, 5))
output_tensor = torch.Tensor.resize_as_(input_tensor, torch.randint(low=0, high=10, size=(2, 3, 5)))