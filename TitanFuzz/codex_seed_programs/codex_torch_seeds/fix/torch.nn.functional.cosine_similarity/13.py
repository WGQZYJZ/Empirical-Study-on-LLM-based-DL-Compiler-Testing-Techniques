'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_similarity\ntorch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-8)\n'
import torch
x1 = torch.randn(100, 128)
x2 = torch.randn(100, 128)
torch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-08)