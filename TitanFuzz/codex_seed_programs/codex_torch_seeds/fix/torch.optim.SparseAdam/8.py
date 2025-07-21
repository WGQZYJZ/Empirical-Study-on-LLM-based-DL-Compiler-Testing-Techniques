'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
import torch.nn as nn
import torch.optim as optim
import torch
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
sparse_adam = optim.SparseAdam([x, y], lr=0.1)
print(sparse_adam)