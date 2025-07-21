"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.binary_cross_entropy_with_logits\ntorch.nn.functional.binary_cross_entropy_with_logits(input, target, weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
input = torch.randn(2, 5, requires_grad=True)
target = torch.empty(2, 5).random_(2)
loss = torch.nn.functional.binary_cross_entropy_with_logits(input, target)
print(loss)
weight = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
loss = torch.nn.functional.binary_cross_entropy_with_logits(input, target, weight=weight)
print(loss)