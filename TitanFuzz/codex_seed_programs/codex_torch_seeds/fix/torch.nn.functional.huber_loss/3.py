"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.huber_loss\ntorch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)\n"
import torch
import torch
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
loss = torch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)
print(loss)
loss.backward()
print(input)
print(input.grad)