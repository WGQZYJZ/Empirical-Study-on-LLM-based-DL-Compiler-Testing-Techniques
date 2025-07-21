'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
from torch.nn import functional as F
import torch
from torch.autograd import Variable
from torch.nn import functional as F
input = Variable(torch.randn(1, 1, 3, 3))
output = F.upsample_nearest(input, size=None, scale_factor=2)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
from torch.nn import functional as F
import torch
from torch.autograd import Variable
from torch.nn import functional as F