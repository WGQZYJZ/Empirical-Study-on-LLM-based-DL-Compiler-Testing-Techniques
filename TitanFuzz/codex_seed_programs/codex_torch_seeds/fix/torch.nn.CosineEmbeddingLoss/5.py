"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineEmbeddingLoss\ntorch.nn.CosineEmbeddingLoss(margin=0.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
x1 = torch.randn(100, 128)
x2 = torch.randn(100, 128)
y = torch.rand(100)
cosine_embedding_loss = nn.CosineEmbeddingLoss()
loss = cosine_embedding_loss(x1, x2, y)
print(loss)