"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.NLLLoss\ntorch.nn.NLLLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
(N, C) = (5, 4)
input = torch.randn(N, C, requires_grad=True)
target = torch.empty(N, dtype=torch.long).random_(C)
loss = torch.nn.NLLLoss()
output = loss(input, target)
print(output)