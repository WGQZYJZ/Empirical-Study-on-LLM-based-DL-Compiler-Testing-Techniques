import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 4, 4)
lazy_instance_norm2d = torch.nn.LazyInstanceNorm2d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)
output_data = lazy_instance_norm2d(input_data)