import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(5, 3, dtype=torch.float32)
(q, r) = torch.geqrf(input_data)