"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
input = torch.randn(2, 3, requires_grad=True)
target = torch.randn(2, 3)
kldivloss = torch.nn.KLDivLoss()
loss = kldivloss(input, target)
print(loss)