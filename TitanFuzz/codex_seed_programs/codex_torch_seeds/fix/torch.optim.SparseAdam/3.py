'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
from torch import nn
import numpy as np
import torch
input_data = torch.randn(100, 10)
target = torch.randint(0, 10, (100,))
optimizer = torch.optim.SparseAdam(params=nn.Linear(10, 10).parameters(), lr=0.1)
for _ in range(100):
    optimizer.zero_grad()
    loss = nn.functional.cross_entropy(nn.Linear(10, 10)(input_data), target)
    loss.backward()
    optimizer.step()
    print(loss.item())