import torch
from torch import nn
from torch.autograd import Variable
a = torch.randn(4, 4)
(top_k_value, top_k_idx) = torch.topk(a, 2)