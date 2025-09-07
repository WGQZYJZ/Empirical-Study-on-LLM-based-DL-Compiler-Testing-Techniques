import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
end = torch.rand(3, 3)
weight = 0.5
_output_tensor = torch.Tensor.lerp_(_input_tensor, end, weight)