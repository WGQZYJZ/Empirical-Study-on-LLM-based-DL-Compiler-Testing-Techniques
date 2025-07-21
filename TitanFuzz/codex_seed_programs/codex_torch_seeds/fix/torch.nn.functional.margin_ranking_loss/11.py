"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.margin_ranking_loss\ntorch.nn.functional.margin_ranking_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
input1 = torch.randn(1)
input2 = torch.randn(1)
target = torch.FloatTensor(1).random_(2)
output = F.margin_ranking_loss(input1, input2, target, margin=0.1, reduction='mean')
print(output)