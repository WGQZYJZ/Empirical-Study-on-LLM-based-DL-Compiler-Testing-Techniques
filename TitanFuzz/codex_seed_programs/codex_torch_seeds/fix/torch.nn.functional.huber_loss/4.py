"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.huber_loss\ntorch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)\n"
import torch
x = torch.randn(10, 3)
y = torch.randn(10, 3)
loss = torch.nn.functional.huber_loss(x, y)
print(loss)
loss = torch.nn.functional.huber_loss(x, y, reduction='none')
print(loss)