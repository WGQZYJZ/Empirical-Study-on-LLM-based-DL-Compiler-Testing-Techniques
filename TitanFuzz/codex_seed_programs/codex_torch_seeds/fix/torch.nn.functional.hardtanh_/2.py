'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh_\ntorch.nn.functional.hardtanh_(input, min_val=-1., max_val=1.)\n'
import torch
from torch.nn import functional as F
import torch
from torch.nn import functional as F
input = torch.randn(3, 3)
print(input)
output = F.hardtanh_(input)
print(output)