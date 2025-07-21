'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
a = torch.randint(0, 10, (2, 3, 4))
b = torch.randint(0, 10, (2, 3, 4))
print(torch.dstack((a, b)))