import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
result = torch.Tensor.isposinf(_input_tensor)