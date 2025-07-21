'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfcx\ntorch.special.erfcx(input, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3, dtype=torch.float64)
y = torch.special.erfcx(x)
print(y)