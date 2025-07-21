"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HingeEmbeddingLoss\ntorch.nn.HingeEmbeddingLoss(margin=1.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
loss = nn.HingeEmbeddingLoss()
output = loss(input, target)
print(output)