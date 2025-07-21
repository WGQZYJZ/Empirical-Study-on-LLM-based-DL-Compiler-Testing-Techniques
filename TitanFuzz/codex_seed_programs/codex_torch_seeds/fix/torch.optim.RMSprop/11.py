'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RMSprop\ntorch.optim.RMSprop(params, lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)\n'
import torch
import numpy as np
x = torch.randn(1, requires_grad=True)
y = (x ** 2)
opt = torch.optim.RMSprop([x], lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)
for i in range(100):
    y = (x ** 2)
    y.backward()
    opt.step()
    opt.zero_grad()
print('x:', x)