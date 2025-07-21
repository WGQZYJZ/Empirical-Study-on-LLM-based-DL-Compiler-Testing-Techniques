'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_similarity\ntorch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-8)\n'
import torch
x1 = torch.randn(1, 3)
x2 = torch.randn(1, 3)
print(x1)
print(x2)
cosine_similarity = torch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-08)
print(cosine_similarity)