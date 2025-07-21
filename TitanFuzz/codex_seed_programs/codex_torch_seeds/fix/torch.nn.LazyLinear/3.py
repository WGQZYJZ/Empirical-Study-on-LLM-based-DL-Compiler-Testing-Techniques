'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
x = torch.randn(1024, 512)
linear = nn.LazyLinear(512, 10)
out = linear(x)
print(out.shape)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyLinear\ntorch.nn.LazyLinear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
x = torch.randn(1024, 512)
linear = nn.LazyLinear(512, 10)