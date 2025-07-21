'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
import numpy as np
x = torch.tensor(np.random.randn(10, 10), requires_grad=True)
y = torch.tensor(np.random.randn(10, 10), requires_grad=True)
optimizer = torch.optim.RAdam([x, y], lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
optimizer.zero_grad()
loss = (x + y).sum()
loss.backward()
optimizer.step()