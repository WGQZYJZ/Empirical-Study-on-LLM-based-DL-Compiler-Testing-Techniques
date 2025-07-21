'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.promote_types\ntorch.promote_types(type1, type2)\n'
import torch
input1 = torch.tensor([1, 2, 3], dtype=torch.float)
input2 = torch.tensor([4, 5, 6], dtype=torch.int)
out = torch.promote_types(input1.dtype, input2.dtype)
print(out)