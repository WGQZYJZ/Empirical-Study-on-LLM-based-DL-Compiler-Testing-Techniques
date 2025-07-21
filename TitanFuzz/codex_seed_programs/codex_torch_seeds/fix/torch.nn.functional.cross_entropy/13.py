"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
N = 100
C = 3
D = 5
S = (N // C)
x = torch.randn(N, D)
y = torch.empty(N, dtype=torch.long).random_(C)
loss = F.cross_entropy(x, y)
print(loss)