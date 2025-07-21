'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.promote_types\ntorch.promote_types(type1, type2)\n'
import torch
x = torch.tensor([1, 2, 3], dtype=torch.float32)
y = torch.tensor([1, 2, 3], dtype=torch.int32)
print(torch.promote_types(x.dtype, y.dtype))