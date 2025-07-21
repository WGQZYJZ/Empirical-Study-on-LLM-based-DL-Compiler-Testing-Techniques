"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_embedding_loss\ntorch.nn.functional.cosine_embedding_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
input1 = torch.randn(100, 128)
input2 = torch.randn(100, 128)
target = torch.randn(100).ge(0).float()
output = F.cosine_embedding_loss(input1, input2, target)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_similarity\ntorch.nn.functional.cosine_similarity(x1, x2, dim=1, eps=1e-8)\n'
import torch
import torch.nn.functional as F
input1 = torch.randn(100, 128)
input2 = torch.randn(100, 128)
output = F.cosine_similarity(input1, input2, dim=1)
print(output)