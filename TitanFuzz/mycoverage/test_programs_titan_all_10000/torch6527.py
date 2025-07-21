import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([True, False, True, False])
output_tensor = torch.Tensor.bitwise_not(input_tensor)