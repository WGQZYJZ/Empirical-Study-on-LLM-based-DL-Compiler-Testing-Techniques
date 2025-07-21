import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_tensor = torch.Tensor.pinverse(input_tensor)