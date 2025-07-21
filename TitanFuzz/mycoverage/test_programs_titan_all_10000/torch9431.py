import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
torch.Tensor.allclose(input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)
torch.Tensor.allclose(input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)
torch.Tensor.allclose(input_tensor, other, rtol=1e-05, atol=1e-05, equal_nan=False)
torch.Tensor.allclose(input_tensor, other, rtol=1e-05, atol=1e-10, equal_nan=False)