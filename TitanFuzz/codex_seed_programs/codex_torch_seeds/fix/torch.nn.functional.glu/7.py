'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.glu\ntorch.nn.functional.glu(input, dim=-1)\n'
import torch
import torch.nn.functional as F
x = torch.randn(3, 4)
print(x)
y = F.glu(x, dim=(- 1))
print(y)