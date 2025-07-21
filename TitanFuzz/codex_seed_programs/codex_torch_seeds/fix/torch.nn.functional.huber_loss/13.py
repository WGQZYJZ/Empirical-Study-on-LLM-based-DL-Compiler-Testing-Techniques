"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.huber_loss\ntorch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)\n"
import torch
input = torch.randn(1, 3)
target = torch.randn(1, 3)
print('Input: ', input)
print('Target: ', target)
loss = torch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)
print('Loss: ', loss)