'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool3d\ntorch.nn.functional.max_pool3d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
dtype = torch.FloatTensor
(N, C, D, H, W) = (2, 3, 4, 5, 6)
x = Variable(torch.randn(N, C, D, H, W).type(dtype), requires_grad=True)
pooled_x = torch.nn.functional.max_pool3d(x, kernel_size=(2, 2, 2), stride=(2, 2, 2), padding=0)
print(pooled_x.size())