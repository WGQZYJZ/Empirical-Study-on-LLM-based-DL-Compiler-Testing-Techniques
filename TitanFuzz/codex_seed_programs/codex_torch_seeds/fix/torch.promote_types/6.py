'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.promote_types\ntorch.promote_types(type1, type2)\n'
import torch
t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([1.0, 2.0, 3.0])
t3 = torch.promote_types(t1.dtype, t2.dtype)
print('t3 =', t3)
t4 = torch.promote_types(t2.dtype, t1.dtype)
print('t4 =', t4)