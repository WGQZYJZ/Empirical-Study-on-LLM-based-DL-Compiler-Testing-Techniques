'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_similarity\ntorch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-8)\n'
import torch
import torch.nn.functional as F
input1 = torch.randn(2, 3)
input2 = torch.randn(2, 3)
output = F.cosine_similarity(input1, input2, dim=1, eps=1e-08)
print(output)