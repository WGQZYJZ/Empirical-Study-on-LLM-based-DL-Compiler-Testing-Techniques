'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.promote_types\ntorch.promote_types(type1, type2)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int)
b = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
torch.promote_types(a.dtype, b.dtype)