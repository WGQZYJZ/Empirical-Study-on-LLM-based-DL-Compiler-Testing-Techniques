import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 5, 5, 5)
lazy_instance_norm_3d = torch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)
output_data = lazy_instance_norm_3d(input_data)