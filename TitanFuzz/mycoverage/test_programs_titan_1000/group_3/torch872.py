import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
result = torch.Tensor.ge(_input_tensor, 2)