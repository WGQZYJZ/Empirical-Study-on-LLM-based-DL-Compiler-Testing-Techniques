'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveLogSoftmaxWithLoss\ntorch.nn.AdaptiveLogSoftmaxWithLoss(in_features, n_classes, cutoffs, div_value=4.0, head_bias=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
'\nimport PyTorch\n'
'\nGenerate input data\n'
in_features = 10
n_classes = 20
cutoffs = [5, 10]
head_bias = True
'\nCall the API torch.nn.AdaptiveLogSoftmaxWithLoss\n'
adaptive_log_softmax_with_loss = nn.AdaptiveLogSoftmaxWithLoss(in_features, n_classes, cutoffs, head_bias=head_bias)
print(adaptive_log_softmax_with_loss)