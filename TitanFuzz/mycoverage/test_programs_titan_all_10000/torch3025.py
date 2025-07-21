import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[3, 4], [5, 6]])
other_data = torch.tensor([[4, 3], [6, 5]])
output_data = torch.Tensor.hypot_(input_data, other_data)