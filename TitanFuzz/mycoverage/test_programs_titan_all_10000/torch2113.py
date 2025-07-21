import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], requires_grad=True)
grad_tensor = torch.Tensor.grad(input_tensor, input_tensor)