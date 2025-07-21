import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_tensor = torch.tensor([[7, 8, 9], [10, 11, 12]])
output_tensor = torch.Tensor.reshape_as(other_tensor, input_tensor)
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])