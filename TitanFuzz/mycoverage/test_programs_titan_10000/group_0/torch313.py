import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([[1.2, 2.3, 3.4], [4.5, 5.6, 6.7]])
output_tensor = torch.Tensor.round(input_tensor)