'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.promote_types\ntorch.promote_types(type1, type2)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3).double()
print(torch.promote_types(x.dtype, y.dtype))