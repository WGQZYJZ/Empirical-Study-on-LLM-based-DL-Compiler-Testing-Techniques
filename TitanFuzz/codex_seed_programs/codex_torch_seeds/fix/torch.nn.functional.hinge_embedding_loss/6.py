"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hinge_embedding_loss\ntorch.nn.functional.hinge_embedding_loss(input, target, margin=1.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(4, 4)
target = torch.tensor([1, 1, (- 1), (- 1)])
loss = F.hinge_embedding_loss(input, target)
print(loss)