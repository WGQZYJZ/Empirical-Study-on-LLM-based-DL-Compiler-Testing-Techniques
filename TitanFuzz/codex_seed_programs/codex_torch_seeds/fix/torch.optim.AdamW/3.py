'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.AdamW\ntorch.optim.AdamW(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.01, amsgrad=False)\n'
import torch
from torch import nn
from torch.optim import AdamW
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
optimizer = AdamW([x, y], lr=0.1, weight_decay=0.01)
print(x.grad)
print(y.grad)
optimizer.zero_grad()
print(x.grad)
print(y.grad)
loss = (x + y)
loss.backward()
print(x.grad)
print(y.grad)
optimizer.step()
print(x.grad)
print(y.grad)
print(x)
print(y)