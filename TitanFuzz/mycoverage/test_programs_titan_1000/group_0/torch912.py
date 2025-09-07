import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3)
end = torch.rand(2, 3)
weight = 0.5
torch.Tensor.lerp(input_tensor, end, weight)