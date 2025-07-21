'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveLogSoftmaxWithLoss\ntorch.nn.AdaptiveLogSoftmaxWithLoss(in_features, n_classes, cutoffs, div_value=4.0, head_bias=False, device=None, dtype=None)\n'
import torch
from torch.nn import AdaptiveLogSoftmaxWithLoss
input = torch.randn(3, 5)
target = torch.empty(3, dtype=torch.long).random_(5)
criterion = AdaptiveLogSoftmaxWithLoss(5, 5, [3, 4])
loss = criterion(input, target)
print(loss)