'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
x = torch.randn(1, 1, 3, 3)
y = F.upsample_nearest(x, size=(5, 5))
print(y)