import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=10, size=(3, 3))
output_tensor = torch.Tensor.tensor_split(input_tensor, 3, dim=0)