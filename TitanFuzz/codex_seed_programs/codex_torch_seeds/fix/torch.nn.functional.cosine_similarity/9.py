'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_similarity\ntorch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-8)\n'
import torch
import torch.nn.functional as F
x1 = torch.rand(1, 3)
x2 = torch.rand(1, 3)
print(x1)
print(x2)
print(F.cosine_similarity(x1, x2, dim=1, eps=1e-08))
'\nTask 4: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2, eps=1e-06, keepdim=False)\n'
print(F.pairwise_distance(x1, x2, p=2, eps=1e-06, keepdim=False))