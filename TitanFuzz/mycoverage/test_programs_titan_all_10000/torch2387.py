import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
splitted_tensor = torch.Tensor.tensor_split(input_tensor, 2, dim=1)
splitted_tensor = torch.Tensor.tensor_split(input_tensor, [1, 2], dim=1)