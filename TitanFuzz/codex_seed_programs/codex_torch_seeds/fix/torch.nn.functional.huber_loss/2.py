"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.huber_loss\ntorch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)\n"
import torch
x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
loss = torch.nn.functional.huber_loss(x, y)
print(loss)