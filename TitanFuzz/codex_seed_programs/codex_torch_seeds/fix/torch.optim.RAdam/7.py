'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
import torch.optim as optim
from torch.autograd import Variable
import numpy as np
x = Variable(torch.FloatTensor([1]), requires_grad=True)
y = Variable(torch.FloatTensor([2]), requires_grad=False)
optimizer = optim.RAdam([x], lr=0.001)
for i in range(100):
    optimizer.zero_grad()
    loss = ((x - y) ** 2)
    loss.backward()
    optimizer.step()
    print(x.data.numpy(), loss.data.numpy())