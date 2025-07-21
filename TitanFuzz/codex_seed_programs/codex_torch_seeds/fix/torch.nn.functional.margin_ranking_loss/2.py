"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.margin_ranking_loss\ntorch.nn.functional.margin_ranking_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch
input1 = torch.randn(100, requires_grad=True)
input2 = torch.randn(100, requires_grad=True)
target = torch.empty(100).random_(2)
loss = torch.nn.functional.margin_ranking_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean')
print(loss)