import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]])
q = 0.5
dim = 0
keepdim = False
result = torch.Tensor.nanquantile(input_tensor, q, dim, keepdim)