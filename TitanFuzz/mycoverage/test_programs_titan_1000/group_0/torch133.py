import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3, 5, 5, requires_grad=True)
lazy_instance_norm = torch.nn.LazyInstanceNorm2d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
output_data = lazy_instance_norm(input_data)