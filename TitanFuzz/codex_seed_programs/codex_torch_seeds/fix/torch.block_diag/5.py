'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
t1 = torch.rand(3, 3)
t2 = torch.rand(4, 4)
t3 = torch.rand(5, 5)
t4 = torch.block_diag(t1, t2, t3)
print(t4)