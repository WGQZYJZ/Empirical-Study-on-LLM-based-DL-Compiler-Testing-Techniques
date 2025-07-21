'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
(n, m) = (10, 20)
x = torch.randn(n, m)
y = torch.randn(n, m)
torch.optim.SparseAdam(x, lr=0.001, betas=(0.9, 0.999), eps=1e-08)