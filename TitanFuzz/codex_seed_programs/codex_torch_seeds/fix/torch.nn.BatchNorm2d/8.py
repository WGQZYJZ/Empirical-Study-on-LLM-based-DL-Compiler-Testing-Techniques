'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.BatchNorm2d\ntorch.nn.BatchNorm2d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
x = torch.randn(2, 3, 4, 4)
bn = nn.BatchNorm2d(3)
print(bn.weight)
print(bn.bias)
y = bn(x)
print(y)
print(bn.running_mean)
print(bn.running_var)
bn = nn.BatchNorm2d(3, affine=False)
print(bn.weight)