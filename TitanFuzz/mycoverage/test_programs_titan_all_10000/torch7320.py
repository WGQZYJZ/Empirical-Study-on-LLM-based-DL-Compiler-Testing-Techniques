import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 1, 1, 1)
is_inference = torch.Tensor.is_inference(input_tensor)