import torch
from torch import nn
from torch.autograd import Variable
if True:
    input = torch.randn(1, 64, 8, 9, 10)
    output_size = (1, 1, 1)
    print(torch.nn.functional.adaptive_max_pool3d(input, output_size))