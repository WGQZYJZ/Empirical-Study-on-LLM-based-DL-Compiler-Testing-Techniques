'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
t1 = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
t2 = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0], dtype=torch.float32)
print(torch.fix(t1))
print(torch.fix(t2))