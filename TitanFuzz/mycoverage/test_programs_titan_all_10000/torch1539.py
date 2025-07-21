import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
output_tensor = torch.Tensor.random_(input_tensor, from_=0, to=1)