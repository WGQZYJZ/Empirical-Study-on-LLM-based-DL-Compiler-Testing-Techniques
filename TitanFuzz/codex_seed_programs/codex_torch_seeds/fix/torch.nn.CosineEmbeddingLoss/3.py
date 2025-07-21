"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineEmbeddingLoss\ntorch.nn.CosineEmbeddingLoss(margin=0.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import numpy as np
import torch
import torch.nn as nn
import numpy as np
np.random.seed(42)
x1 = np.random.rand(100, 10)
x2 = np.random.rand(100, 10)
y = np.random.randint(0, 2, size=100)
x1 = torch.from_numpy(x1).float()
x2 = torch.from_numpy(x2).float()
y = torch.from_numpy(y).float()
loss = nn.CosineEmbeddingLoss()
loss_value = loss(x1, x2, y)
print(loss_value)