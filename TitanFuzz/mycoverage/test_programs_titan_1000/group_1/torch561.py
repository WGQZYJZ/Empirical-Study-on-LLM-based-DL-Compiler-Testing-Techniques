import torch
from torch import nn
from torch.autograd import Variable
x1 = torch.randn(100, 128)
x2 = torch.randn(200, 128)
dist = torch.cdist(x1, x2, p=2.0, compute_mode='use_mm_for_euclid_dist_if_necessary')