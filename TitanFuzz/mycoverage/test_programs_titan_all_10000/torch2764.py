import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(12).reshape(3, 4)
output_tensor = torch.Tensor.tensor_split(input_tensor, 2, dim=0)