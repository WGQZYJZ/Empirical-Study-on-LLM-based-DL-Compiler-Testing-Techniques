'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.promote_types\ntorch.promote_types(type1, type2)\n'
import torch
x = torch.randn(5, 5)
print(x.type())
y = torch.tensor([1, 2, 3, 4, 5])
print(y.type())
z = torch.promote_types(x.dtype, y.dtype)
print(z)