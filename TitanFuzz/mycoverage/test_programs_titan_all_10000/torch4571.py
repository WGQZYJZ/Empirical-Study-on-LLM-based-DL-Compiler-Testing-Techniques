import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]])
output_tensor = torch.Tensor.not_equal(input_tensor, other=torch.tensor(1))