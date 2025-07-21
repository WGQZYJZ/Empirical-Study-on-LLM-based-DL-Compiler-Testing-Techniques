"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineEmbeddingLoss\ntorch.nn.CosineEmbeddingLoss(margin=0.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch
x1 = torch.rand(3, 4)
x2 = torch.rand(3, 4)
y = torch.tensor([1, 0, (- 1)])
loss = nn.CosineEmbeddingLoss()
output = loss(x1, x2, y)
print(output)