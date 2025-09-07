import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
output_tensor = torch.Tensor.divide(input_tensor, 2.0)