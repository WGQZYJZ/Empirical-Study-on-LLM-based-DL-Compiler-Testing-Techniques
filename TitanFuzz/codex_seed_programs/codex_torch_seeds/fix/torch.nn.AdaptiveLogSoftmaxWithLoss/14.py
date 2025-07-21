'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveLogSoftmaxWithLoss\ntorch.nn.AdaptiveLogSoftmaxWithLoss(in_features, n_classes, cutoffs, div_value=4.0, head_bias=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(4, 4)
target = torch.randint(low=0, high=4, size=(4,))
criterion = nn.AdaptiveLogSoftmaxWithLoss(4, 4, [2, 3])
loss = criterion(input, target)
print(loss)