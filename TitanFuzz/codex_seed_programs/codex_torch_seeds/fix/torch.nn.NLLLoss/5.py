"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.NLLLoss\ntorch.nn.NLLLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
loss = nn.NLLLoss()
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
output = loss(input, target)
output.backward()
print(input)
print(target)
print(output)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.NLLLoss\ntorch.nn.NLLLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F