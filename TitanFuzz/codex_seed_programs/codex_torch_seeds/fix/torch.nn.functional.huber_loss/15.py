"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.huber_loss\ntorch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)\n"
import torch
input = torch.randn(10, 3)
target = torch.randn(10, 3)
print(f'Input: {input}')
print(f'Target: {target}')
loss = torch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)
print(f'Loss: {loss}')