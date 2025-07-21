"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input = Variable(torch.randn(1, 1, 3, 3))
print(input)
upsample = nn.Upsample(scale_factor=2, mode='nearest')
print(upsample(input))
upsample = nn.Upsample(size=[5, 5], mode='nearest')
print(upsample(input))