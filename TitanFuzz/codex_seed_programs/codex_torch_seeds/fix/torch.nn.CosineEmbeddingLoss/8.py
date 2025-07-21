"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineEmbeddingLoss\ntorch.nn.CosineEmbeddingLoss(margin=0.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input1 = torch.randn(100, 128)
input2 = torch.randn(100, 128)
target = torch.empty(100, dtype=torch.long).random_(2)
loss = nn.CosineEmbeddingLoss()
output = loss(input1, input2, target)
print(output)