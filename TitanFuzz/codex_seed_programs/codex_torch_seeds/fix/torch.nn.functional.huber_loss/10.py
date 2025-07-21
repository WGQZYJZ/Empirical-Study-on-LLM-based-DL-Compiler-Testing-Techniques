"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.huber_loss\ntorch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)\n"
import torch
import torch.nn.functional as F
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
loss = F.huber_loss(input, target)
print(loss)
loss = F.smooth_l1_loss(input, target)
print(loss)