'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.wait\ntorch.jit.wait(future)\n'
import torch
import time
x = torch.tensor([1, 2, 3])
future = torch.jit._fork(torch.add, x, x)
torch.jit.wait(future)
print(future.wait())