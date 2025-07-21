import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4, 4)
input = torch.randn(4, 4, 4)
output = torch.nn.functional.local_response_norm(input, size=2, alpha=0.0001, beta=0.75, k=1.0)