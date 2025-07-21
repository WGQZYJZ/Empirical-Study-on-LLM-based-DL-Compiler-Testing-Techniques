"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HingeEmbeddingLoss\ntorch.nn.HingeEmbeddingLoss(margin=1.0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
input_data = torch.tensor([[1.0, (- 1.0), 1.0], [(- 1.0), 1.0, (- 1.0)]])
target = torch.tensor([[1.0, 1.0, (- 1.0)], [1.0, 1.0, (- 1.0)]])
loss_fn = nn.HingeEmbeddingLoss(margin=1.0)
loss = loss_fn(input_data, target)
print(loss)