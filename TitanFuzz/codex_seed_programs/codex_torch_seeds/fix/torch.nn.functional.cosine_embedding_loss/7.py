"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cosine_embedding_loss\ntorch.nn.functional.cosine_embedding_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch
input1 = torch.randn(100, 128)
input2 = torch.randn(100, 128)
target = torch.randn(100).ge(0).float()
output = torch.nn.functional.cosine_embedding_loss(input1, input2, target)
print(output)