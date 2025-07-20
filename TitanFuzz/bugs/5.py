import torch

a = torch.tensor(float('nan'))

b = a.clone().cpu().type(torch.int32)
c = a.clone().cuda().type(torch.int32)
print(b) # tensor(-2147483648, dtype=torch.int32)
print(c) # tensor(0, device='cuda:0', dtype=torch.int32)