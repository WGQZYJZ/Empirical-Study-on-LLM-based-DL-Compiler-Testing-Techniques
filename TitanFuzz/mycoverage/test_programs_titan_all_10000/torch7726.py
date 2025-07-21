import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[True, False, True], [False, False, False]])
result = torch.Tensor.bitwise_xor(input_tensor, other=True)