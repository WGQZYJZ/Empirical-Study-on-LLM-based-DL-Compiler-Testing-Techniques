import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.randn(1, 1, 3, 3)
input_tensor = torch.Tensor(input_data)
expm1_out = torch.Tensor.expm1(input_tensor)