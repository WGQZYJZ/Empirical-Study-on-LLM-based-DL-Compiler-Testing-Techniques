import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1, 2, 3, 4, 5])
result = torch.Tensor.ne(input_tensor, other=1)