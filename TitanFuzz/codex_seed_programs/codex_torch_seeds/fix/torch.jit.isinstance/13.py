'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
import numpy as np
a = torch.randn(3, 3)
b = torch.randn(3, 2)
c = torch.randint(0, 2, (3, 3))
d = torch.randint(0, 2, (3, 3))
e = torch.randn(3, 3)
f = torch.randn(3, 3)
torch.jit.isinstance(a, torch.Tensor)
torch.jit.isinstance(b, torch.Tensor)
torch.jit.isinstance(c, torch.Tensor)
torch.jit.isinstance(d, torch.Tensor)
torch.jit.isinstance(e, torch.Tensor)
torch.jit.isinstance(f, torch.Tensor)