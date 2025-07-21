'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.slogdet\ntorch.slogdet(input)\n'
import torch
input = torch.randn(2, 3, 3, dtype=torch.float64)
print(input)
(s, logdet) = torch.slogdet(input)
print(s)
print(logdet)