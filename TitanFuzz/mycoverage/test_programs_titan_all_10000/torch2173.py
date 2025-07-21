import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 5)
(max_value, max_idx) = torch.max(input, dim=1)
(max_value, max_idx) = torch.max(input, dim=1, keepdim=True)
(max_value, max_idx) = torch.max(input, dim=1, keepdim=True, out=(torch.zeros(3, 1), torch.zeros(3, 1, dtype=torch.long)))