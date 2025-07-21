import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.normal_(input_tensor, mean=0, std=1)