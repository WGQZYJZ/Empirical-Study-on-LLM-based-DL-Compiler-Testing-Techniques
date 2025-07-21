"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.huber_loss\ntorch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)\n"
import torch
import torch
x = torch.rand(1, 1)
y = torch.rand(1, 1)
loss = torch.nn.functional.huber_loss(x, y, reduction='mean', delta=1.0)
print('loss = ', loss)