import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
result = torch.Tensor.subtract(input_tensor, other)