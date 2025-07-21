'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
a = torch.tensor([[True, True], [False, False]])
print(a)
b = torch.bitwise_not(a)
print(b)