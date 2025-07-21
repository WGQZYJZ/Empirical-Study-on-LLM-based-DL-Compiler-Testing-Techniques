import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
(min_value, min_idx) = torch.min(x, dim=1)
(min_value, min_idx) = torch.min(x, dim=0)
(min_value, min_idx) = torch.min(x, dim=1, keepdim=True)
(min_value, min_idx) = torch.min(x, dim=0, keepdim=True)