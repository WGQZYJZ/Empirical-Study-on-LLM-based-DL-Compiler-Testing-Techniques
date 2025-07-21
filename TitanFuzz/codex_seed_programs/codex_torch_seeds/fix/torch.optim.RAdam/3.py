'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
from torch.optim import RAdam
x = torch.tensor(1.0, requires_grad=True)
optimizer = RAdam([x], lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
for epoch in range(100):
    optimizer.zero_grad()
    loss = (x ** 2)
    loss.backward()
    optimizer.step()
    print('Epoch {}, x = {:.6f}, loss = {:.6f}'.format(epoch, x.item(), loss.item()))