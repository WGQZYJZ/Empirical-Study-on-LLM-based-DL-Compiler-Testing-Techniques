"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.binary_cross_entropy\ntorch.nn.functional.binary_cross_entropy(input, target, weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
input = torch.tensor([[1, 0, 1, 0], [1, 1, 0, 1]], dtype=torch.float32)
target = torch.tensor([[1, 1, 0, 0], [0, 1, 1, 0]], dtype=torch.float32)
print(torch.nn.functional.binary_cross_entropy(input, target))