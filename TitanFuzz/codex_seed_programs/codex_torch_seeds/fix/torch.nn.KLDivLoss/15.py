"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
criterion = nn.KLDivLoss()
loss = criterion(input, target)
print(loss)
loss.backward()
print(input.grad)