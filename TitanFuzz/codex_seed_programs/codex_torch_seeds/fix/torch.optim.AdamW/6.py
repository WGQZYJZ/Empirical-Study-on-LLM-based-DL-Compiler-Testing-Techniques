'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.AdamW\ntorch.optim.AdamW(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.01, amsgrad=False)\n'
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
x = torch.rand(10, requires_grad=True)
y = torch.rand(10, requires_grad=True)
optimizer = optim.AdamW([x, y], lr=0.001)
optimizer.zero_grad()
output = torch.sum((x + y))
output.backward()
optimizer.step()
print(x.grad)
print(y.grad)