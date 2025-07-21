'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch
x = torch.randn(1, 3, requires_grad=True)
y = torch.randn(1, 3, requires_grad=True)
pairwise_distance = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
distance = pairwise_distance(x, y)
print(distance)
distance.backward()
print(x.grad)
print(y.grad)