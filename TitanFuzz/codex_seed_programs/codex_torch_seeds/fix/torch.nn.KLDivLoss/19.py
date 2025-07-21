"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
input = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
target = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]])
loss = torch.nn.KLDivLoss()
output = loss(input, target)
print(output)